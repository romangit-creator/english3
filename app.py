import json
import random
from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'
socketio = SocketIO(app, cors_allowed_origins="*")

# Загружаем базу слов
with open('words.json', 'r', encoding='utf-8') as f:
    words_db = json.load(f)

# Функция для одиночного режима (1 правильное, 3 случайных)
def get_random_word_with_options():
    ru_word = random.choice(list(words_db.keys()))
    correct_en = words_db[ru_word]
    all_en_words = list(words_db.values())
    all_en_words.remove(correct_en)
    
    options = random.sample(all_en_words, min(3, len(all_en_words)))
    options.append(correct_en)
    random.shuffle(options)
    return ru_word, correct_en, options

# --- РОУТЫ СТРАНИЦ ---
@app.route('/')
def single_player():
    ru_word, correct_en, options = get_random_word_with_options()
    return render_template('single.html', ru_word=ru_word, correct=correct_en, options=options)

@app.route('/multi')
def multi_player():
    return render_template('multi.html')


# --- ЛОГИКА МУЛЬТИПЛЕЕРА (WebSockets) ---
players = []
game_state = {
    "round": 0,
    "max_rounds": 10,
    "current_word_ru": "",
    "current_word_en": "",
    "scores": {}
}

@socketio.on('join')
def handle_join(data):
    username = data['username']
    if len(players) < 2 and username not in players:
        players.append(username)
        game_state["scores"][username] = 0
        join_room('game_room')
        emit('message', {'msg': f'👋 {username} в игре! ({len(players)}/2)'}, room='game_room')
        
        if len(players) == 2:
            emit('message', {'msg': '🚀 Игроки найдены! Начинаем...'}, room='game_room')
            start_next_round()
    elif username in players:
        emit('message', {'msg': '❌ Вы уже в игре.'})
    else:
        emit('message', {'msg': '❌ Комната заполнена!'})

def start_next_round():
    game_state["round"] += 1
    if game_state["round"] > game_state["max_rounds"]:
        emit('game_over', {'scores': game_state["scores"]}, room='game_room')
        players.clear()
        game_state["scores"].clear()
        game_state["round"] = 0
    else:
        ru_word = random.choice(list(words_db.keys()))
        game_state["current_word_ru"] = ru_word
        game_state["current_word_en"] = words_db[ru_word]
        emit('new_round', {'round': game_state["round"], 'word': ru_word}, room='game_room')

@socketio.on('submit_answer')
def handle_answer(data):
    if game_state["round"] == 0:
        return  # Игра еще не идет
    
    username = data['username']
    answer = data['answer'].strip().lower()
    correct_answer = game_state["current_word_en"]
    
    if answer == correct_answer:
        # Правильный ответ
        game_state["scores"][username] += 1
        emit('round_winner', {
            'winner': username, 
            'word': correct_answer, 
            'scores': game_state["scores"]
        }, room='game_room')
        start_next_round()
    else:
        # Неправильный ответ - выводим сообщение с именем игрока
        emit('message', {
            'msg': f'❌ {username}, неправильный ответ!'
        }, room='game_room')

# запуск сервера
# if __name__ == "__main__":
#    port = int(os.environ.get("PORT", 5000))
#    socketio.run(app, host='0.0.0.0', port=port)

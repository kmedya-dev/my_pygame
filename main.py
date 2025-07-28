from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key' # Replace with a strong secret key in production

@app.route('/')
def index():
    session['game_state'] = 'start'
    return render_template('game.html', message="Welcome to the Text Adventure! You find yourself in a dark room. There is a door to your left and a door to your right.")

@app.route('/play', methods=['POST'])
def play():
    choice = request.form['choice'].lower()

    if session.get('game_state') == 'start':
        if choice == 'left':
            session['game_state'] = 'left_door'
            return render_template('game.html', message="You chose the left door and find a treasure chest! Congratulations, you win!")
        elif choice == 'right':
            session['game_state'] = 'right_door'
            return render_template('game.html', message="You chose the right door and fell into a pit. Game Over.")
        else:
            return render_template('game.html', message="Invalid choice. You are stuck in the room forever. Game Over.")
    else:
        return render_template('game.html', message="Game over. Please refresh to play again.")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

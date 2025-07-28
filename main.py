from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key' # Replace with a strong secret key in production

@app.route('/')
def index():
    session['game_state'] = 'text_adventure_start' # New state for clarity
    return render_template('game.html', message="Welcome to the Text Adventure! You find yourself in a dark room. There is a door to your left and a door to your right.", placeholder_text="Type your choice (left/right)", game_title="Text Adventure Game")

@app.route('/play', methods=['POST'])
def play():
    user_input = request.form['choice'].lower()

    current_game_state = session.get('game_state')

    if current_game_state == 'text_adventure_start':
        if user_input == 'left':
            session['game_state'] = 'guessing_game_start'
            session['secret_number'] = random.randint(1, 100)
            session['guesses_taken'] = 0
            return render_template('game.html', message="You chose the left door and found a treasure chest! Now, let's play a guessing game. I'm thinking of a number between 1 and 100. What's your guess?", placeholder_text="Type your guess (1-100)", game_title="Number Guessing Game")
        elif user_input == 'right':
            session['game_state'] = 'game_over' # New state for clarity
            return render_template('game.html', message="You chose the right door and fell into a pit. Game Over. Refresh to play again.", placeholder_text="Game Over", game_title="Game Over")
        else:
            session['game_state'] = 'game_over'
            return render_template('game.html', message="Invalid choice. You are stuck in the room forever. Game Over. Refresh to play again.", placeholder_text="Game Over", game_title="Game Over")

    elif current_game_state == 'guessing_game_start' or current_game_state == 'guessing_game_playing':
        try:
            guess = int(user_input)
            secret_number = session['secret_number']
            session['guesses_taken'] += 1
            guesses_taken = session['guesses_taken']

            if guess < secret_number:
                message = f"Too low! You've taken {guesses_taken} guesses. Try again."
                session['game_state'] = 'guessing_game_playing'
            elif guess > secret_number:
                message = f"Too high! You've taken {guesses_taken} guesses. Try again."
                session['game_state'] = 'guessing_game_playing'
            else:
                message = f"You got it! The number was {secret_number}. It took you {guesses_taken} guesses. Game Over. Refresh to play again."
                session['game_state'] = 'game_over' # Game over after guessing game win
            return render_template('game.html', message=message, placeholder_text="Game Over", game_title="Number Guessing Game")
        except ValueError:
            message = "Please enter a valid number."
            return render_template('game.html', message=message, placeholder_text="Enter a number", game_title="Number Guessing Game")

    elif current_game_state == 'game_over':
        return render_template('game.html', message="Game over. Please refresh to play again.", placeholder_text="Game Over", game_title="Game Over")

    else: # Fallback for unexpected state
        session['game_state'] = 'game_over'
        return render_template('game.html', message="An unexpected error occurred. Game over. Please refresh to play again.", placeholder_text="Game Over", game_title="Game Over")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
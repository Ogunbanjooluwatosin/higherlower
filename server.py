import random
from flask import Flask

app = Flask(__name__)


@app.route("/")
def h1():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' alt= 'A gif'>"


random_number = random.randint(0, 9)


@app.route("/URL/<int:number>")
def number(number):
    if number < random_number:
        return "<h1 style='color:red'>Too low,try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif',alt='a gif'>"
    elif number > random_number:
        return "<h1 style='color:blue'>Too high,try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif',alt='a gif'>"
    else:
        return "<h1 style='color:green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif',alt='a gif'>"


if __name__ == "__main__":
    app.run(debug=True)

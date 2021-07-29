from flask import Flask, render_template
import random as rd

application = Flask(__name__)

quotes = list()

quotes.append(["When you assume negative intent, you're angry. If you take away that anger and assume positive intent, " \
       "you will be amazed. Your emotional quotient goes up because you are no longer almost random in your response." ,0])

quotes.append(["Love is a beautiful feeling.",0])

rd.seed(1)


# Home Page
@application.route('/')
def home():
    num = rd.randint(0,9)
    return render_template('home.html', id=num, quote=quotes[num][0], likes=quotes[num][1] )


@application.route('/updateLike/<id>', methods=['GET'])
def updateLike(id):
    quotes[int(id)][1] += 1
    return "OK"


# Main Function
if __name__ == '__main__':
    application.run()





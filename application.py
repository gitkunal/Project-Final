from flask import Flask, render_template
import random as rd

application = Flask(__name__)

quotes = list()

quotes.append(["When you assume negative intent, you're angry. If you take away that anger and assume positive intent, " \
       "you will be amazed. Your emotional quotient goes up because you are no longer almost random in your response." ,0])

quotes.append(["Carry out a random act of kindness, with no expectation of reward, safe in the knowledge that one day someone " \
       "might do the same for you.",0])

quotes.append(["Together we can change the world, just one random act of kindness at a time.",0])

quotes.append(["We can all fight against loneliness by engaging in random acts of kindness." ,0])

quotes.append(["Sometimes in life, random things can blind-side you.",0])

quotes.append(["Creativity is the process of having original ideas that have value. It is a process; it's not random.",
               0])

quotes.append(["In all natural disasters through time, man needs to attach meaning to tragedy, no matter how random "
               "and inexplicable the event is.",0])

quotes.append(["My personal style is kind of random; it's always changing - I'm a Pisces! Sometimes I like one particular "
               "style for a season, and the next season I will dress totally different.",0])

quotes.append(["There's good random, and there's bad random. There's good silly and there's bad silly, and you've gotta "
               "know the difference.",0])

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





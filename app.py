from flask import Flask, render_template
import os
from random import randint

IMG_FOLDER = os.path.join('static', 'images')

app = Flask(__name__)


quotes = ["Logic will get you from A to B. Imagination will take you everywhere."]
quotes.append("There are 10 kinds of people. Those who know binary and those who don't.")
quotes.append("There are two ways of constructing a software design. One way is to make it so simple that there are obviously no deficiencies and the other is to make it so complicated that there are no obvious deficiencies.")
quotes.append("It's not that I'm so smart, it's just that I stay with problems longer.")
quotes.append("It is pitch dark.  You are likely to be eaten by a grue.")

@app.route('/')
def hello():
    img_filename = os.path.join(IMG_FOLDER, 'image.gif')
    idx = randint(0,4)
    quote = quotes[idx]
    return render_template('template.html', user_image=img_filename, display_text=quote)
    
    
if __name__ == '__main__':
    app.run(debug=True)
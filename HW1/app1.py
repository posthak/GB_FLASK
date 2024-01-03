from flask import Flask
from flask import render_template

app = Flask(__name__)
# html = """<h1>Hi, my name ist Mic</h1>
# <p>Already many years I create sites on Flask<br/>Have a look.</p>
# """

# @app.route('/')
# def index():
#     return 'Hi!'

@app.route('/')
def main():
    context = {'title': 'Одежда'}
    return render_template('clothes.html', **context)

@app.route('/shoes/')
def shoes():
    context = {'title': 'Обувь'}
    return render_template('shoes.html', **context)

@app.route('/jacket/')
def jacket():
    context = {'title': 'Куртка'}
    return render_template('jacket.html', **context)


if __name__ == '__main__':
    app.run(debug=True)

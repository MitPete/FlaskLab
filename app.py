from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def hello_world():
    return '''
    <p>Genevieve M.: afaik</p>
    <p>John D.: brb</p>
    <p>Alice W.: lol</p>
    '''  # Add more entries as per your classmates' preferences

@app.route('/peter')
def personal_greeting():
    return render_template('template.html')

if __name__ == '__main__':
    app.run()

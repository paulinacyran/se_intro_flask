from flask import Flask
app = Flask(__name__)

moje_imie = 'Paulina'
noje_zwierze = 'Kot'

@app.route('/')
def hello_world():
    return 'Hello, World ' + moje_imie + ' !'

@app.route('/kto')
def kto():
    return moje_zwierze


@app.route('/wiadomosc')
def wiadomosc():
    return 'Hello, World!'

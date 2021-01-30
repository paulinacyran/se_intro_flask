from flask import Flask
from flask import request
app = Flask(__name__)

moje_imie = 'Paulina'
moje_zwierze = 'Kot'

@app.route('/')
def hello_world():
    return 'Hello, World ' + moje_imie + ' !'

@app.route('/kto')
def kto():
    return moje_zwierze

# http://127.0.0.1:5000/oblicz?l1=10&l2=20&op=plus
@app.route('/oblicz')
def oblicz():
    l1 = int(request.args.get('l1'))
    l2 = int(request.args.get('l2'))
    op = request.args.get('op')
    if op == "plus":
        s = l1 + l2
        return f'{s}'
    return ""

@app.route('/podziel')
def podziel():
    l1 = int(request.args.get('l1'))
    l2 = int(request.args.get('l2'))
    op = request.args.get('op')
    if op == "ukosnik":
        s = l2 / l1
        return f'{s}'
    return ""

@app.route('/wiadomosc')
def wiadomosc():
    return 'Hello, World!'

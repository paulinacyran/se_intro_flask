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
    l1_arg = request.args.get('l1')
    if l1_arg is None:
        return 'brak argumentu l1'
    l1 = int(l1_arg)

    l2_arg = request.args.get('l2')
    l2 = int(l2_arg)
    op = request.args.get('op')
    if op == 'plus':
        s = l1 + l2
        return f'{s}'
    return ""

    # l1 = int(request.args.get('l1'))
    # l2 = int(request.args.get('l2'))
    # op = request.args.get('op')
    # if op == "plus":
    #     s = l1 + l2
    #     return f'{s}'
    # return ""

# http://127.0.0.1:5000/podziel?l1=10&l2=20&op=ukosnik
@app.route('/podziel')
def podziel():
    l1_arg = request.args.get('l1')
    if l1_arg is None:
        return 'brak argumentu l1'
    l1 = int(l1_arg)

    l2_arg = request.args.get('l2')
    l2 = int(l2_arg)
    op = request.args.get('op')
    if op == 'ukosnik':
        s = l1 / l2
        return f'{s}'
    return ""

    # l1 = int(request.args.get('l1'))
    # l2 = int(request.args.get('l2'))
    # op = request.args.get('op')
    # if op == "ukosnik":
    #     s = l2 / l1
    #     return f'{s}'
    # return ""

@app.route('/wiadomosc')
def wiadomosc():
    return 'Hello, World!'

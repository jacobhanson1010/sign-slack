import os
import threading
from flask import Flask, request

app = Flask(__name__)
on_off = False
event = None


def turn_on():
    global on_off
    global event

    if event is not None:
        event.cancel()
        print('turn_off() schedule canceled')

    on_off = True
    print('sign turned on for 15 minutes')
    event = threading.Timer(900, turn_off)
    event.start()
    print('turn_off() scheduled')


def turn_off():
    global on_off
    global event

    on_off = False
    print('sign turned off')
    event.cancel()
    print('turn_off() schedule canceled')


@app.route('/', methods=['POST'])
def slash_command():
    text = str(request.form.get('text')).lower().strip()
    if text == 'on':  # set sign to on
        turn_on()
        return 'sign turned on for 15 minutes!'
    elif text == 'off':  # set sign to off
        turn_off()
        return 'sign turned off!'

    print('invalid request text was ' + text)
    return '[' + text + '] is not a valid command!'


@app.route('/', methods=['GET'])
def get_status():
    global on_off
    return str(on_off)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

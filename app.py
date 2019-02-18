import os
import threading
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)
on_off = False
event = None


def format_response(response, ephemeral=False):
    response_dict = {'text': response}
    if ephemeral == True:
        response_dict['response_type'] = 'ephemeral'
    else:
        response_dict['response_type'] = 'in_channel'

    return jsonify(response_dict)


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
    if event is not None:
        event.cancel()
        print('turn_off() schedule canceled')


@app.route('/', methods=['POST'])
def slash_command():
    text = str(request.form.get('text')).lower().strip()
    user_name = str(request.form.get('user_name')).strip()
    token = str(request.form.get('token')).strip()

    if token != str(os.environ.get('SLACK_TOKEN', 'token')):
        return make_response('invalid slack token', 401)

    if text == 'on':  # set sign to on
        turn_on()
        return format_response(user_name + ' turned the sign on for 15 minutes!')
    elif text == 'off':  # set sign to off
        turn_off()
        return format_response(user_name + ' turned the sign off!')
    elif text == '':  # set sign to on
        turn_on()
        return format_response(user_name + ' turned the sign on for 15 minutes!')

    print('invalid request text was ' + text)
    return format_response('[' + text + '] is not a valid command!', True)


@app.route('/', methods=['GET'])
def get_status():
    global on_off
    return str(on_off)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

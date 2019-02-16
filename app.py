import os

from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def slash_command():
    text = str(request.form.get('&text'))
    if text == 'on':  # set sign to on
        print('sign turned on')
        return 'sign turned on!'
    elif text == 'off':  # set sign to off
        print('sign turned off')
        return 'sign turned off!'

    print('invalid request text was ' + text)
    return text + ' is not a valid command!'


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 33507))
    app.run(host='0.0.0.0', port=33507, debug=True)

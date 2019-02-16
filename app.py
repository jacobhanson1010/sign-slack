from flask import Flask

app = Flask(__name__)


@app.route('/')
def slash_command():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)

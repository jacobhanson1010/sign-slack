## sign-slack
This repo includes the two python scripts that support controlling the sign through slack.

### app.py
This script runs a Flask server (in Heroku) that listens for the /sign webhook coming from slack. It holds a boolean value representing the state of the sign.

### sign.py
Simple script that performs a GET request to app.py to get the current boolean state of the sign. If the state changes, modify the GPIO output appropriately.

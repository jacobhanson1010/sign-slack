#!sign/bin/python

import time
import requests
import RPi.GPIO as GPIO

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(17, GPIO.OUT)

    try:
        on_off = False
        while True:
            on_off_temp = requests.get('https://sign-slack.herokuapp.com/').text == 'True'
            if on_off != on_off_temp:
                print('on_off state changed from ' + str(on_off) + ' to ' + str(on_off_temp))
                on_off = on_off_temp

                if on_off:
                    GPIO.output(17, GPIO.HIGH)
                else:
                    GPIO.output(17, GPIO.LOW)

            time.sleep(5)

    except KeyboardInterrupt:
        print('interrupted!')
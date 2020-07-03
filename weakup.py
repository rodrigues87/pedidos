import threading
import requests

interval = 4 * 60


def myPeriodicFunction():
    requests.get('https://azmel.herokuapp.com/')


def startTimer():
    threading.Timer(interval, startTimer).start()
    myPeriodicFunction()


startTimer()

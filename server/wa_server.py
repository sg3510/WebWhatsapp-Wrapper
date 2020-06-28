import sys 
sys.path.append('..')
from flask import Flask
from webwhatsapi import WhatsAPIDriver
import time, threading
from resettabletimer import ResettableTimer
app = Flask(__name__)

driver_running = False
webdriver_logged_in = False

## Decorator for driver status handling
def webdriver_mgmt(func):
    def wrapper_webdriver_mgmt():
    	if driver_running:
        	func()
    	else:
    		driver = WhatsAPIDriver()
    		driver_running = True
    		func()
    return wrapper_webdriver_mgmt


def is_wa_loggedin():
	#get_status
	return false

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(host='0.0.0.0')
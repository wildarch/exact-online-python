#!/usr/bin/env python3
from flask import Flask, request
from urllib import parse
import requests
import os
import sys
import time
import configparser
import webbrowser

module_dir = os.path.dirname(os.path.abspath(sys.modules[__name__].__file__))

oauth_url = 'https://start.exactonline.nl/api/oauth2/auth'
token_url = 'https://start.exactonline.nl/api/oauth2/token'
client_id = '28554901-0075-4e86-92f4-76764817b4f3'
secret = 'CsiVKM9ou5Fy'
redirect_uri = 'https://localhost/exactauth'
login_url = '{0}?client_id={1}&redirect_uri={2}&response_type=code&force_login=0'.format(oauth_url, parse.quote(client_id), parse.quote(redirect_uri))
force_login = 0

# Reduce logging level so Flask doesn't clutter the console
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

class Server:
    def __init__(self):
        self.app = Flask(__name__)

        # The redirect route
        @self.app.route('/exactauth')
        def oauth_success():
            # Shut the server down once we have the code
            self.code = request.args.get('code')
            shutdown = request.environ.get('werkzeug.server.shutdown')
            shutdown()
            return "Login was successful. You may close this window/tab now."


def get_code():
    # Starts the server to capture the code
    server = Server()
    webbrowser.open_new_tab(login_url) #Send the user to the Auth URL
    cert = os.path.join(module_dir, 'localhost.cert')
    key = os.path.join(module_dir, 'localhost.key')
    server.app.run(port=443, debug=False, ssl_context=(cert, key))
    return server.code


def get_token():
    saved_token = get_saved_token()
    if saved_token is not None:
        return saved_token

    print("No saved token found")
    code = get_code()
    # Sends a POST request to retrieve the access token
    data = {
        'code': code,
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code',
        'client_id': client_id,
        'client_secret': secret
    }
    json = requests.post(token_url, data=data).json()
    token = json['access_token']
    save_token(token)
    return token


def get_saved_token():
    try:
        config = configparser.ConfigParser()
        config.read('token.ini')
        if 'main' not in config:
            print("Format error in token.ini")
        main = config['main']
        if 'token' in main and 'timestamp' in main:
            timestamp = float(main['timestamp'])
            now = time.time()
            if now - timestamp < 600: #10 minutes
                #print("main token found!")
                return main['token']
    except Exception as e:
        print(e)


def save_token(token):
    config = configparser.ConfigParser()
    config['main'] = {
        'token': token,
        'timestamp': time.time()
    }
    with open('token.ini', 'w') as file:
        config.write(file)



if __name__ == '__main__':
    if os.geteuid() != 0:
        print("You must run this script as root!")
        os._exit(1)
    #print(login_url)
    token = get_token()
    sys.stdout.write(token)

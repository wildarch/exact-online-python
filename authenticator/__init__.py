#!/usr/bin/env python3
from flask import Flask, request
from urllib import parse
import requests
import os
import sys
import time
import configparser
import webbrowser
import logging

module_dir = os.path.dirname(os.path.abspath(sys.modules[__name__].__file__))

oauth_url = 'https://start.exactonline.nl/api/oauth2/auth'
token_url = 'https://start.exactonline.nl/api/oauth2/token'


def login_url(client_id, redirect_uri):
    return '{0}?client_id={1}&redirect_uri={2}&response_type=code&force_login=0'.format(oauth_url,
                                                                                        parse.quote(client_id),
                                                                                        parse.quote(redirect_uri))

force_login = 0

# Reduce logging level so Flask doesn't clutter the console
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


def get_code(client_id, redirect_uri):
    # Starts the server to capture the code
    server = Server()
    webbrowser.open_new_tab(login_url(client_id, redirect_uri))
    cert = os.path.join(module_dir, 'localhost.cert')
    key = os.path.join(module_dir, 'localhost.key')
    server.app.run(port=443, debug=False, ssl_context=(cert, key))
    return server.code


def acquire_token(code, client_id, redirect_uri, secret):
    data = {
        'code': code,
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code',
        'client_id': client_id,
        'client_secret': secret
    }
    json = requests.post(token_url, data=data).json()
    return json['access_token']


def get_token(client_id, redirect_uri, secret):
    saved_token = get_saved_token()
    if saved_token is not None:
        return saved_token

    print("No saved token found")
    code = get_code(client_id, redirect_uri)
    # Sends a POST request to retrieve the access token
    token = acquire_token(code, client_id, redirect_uri, secret)
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
            if now - timestamp < 600:  # 10 minutes
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
    token = get_token()
    sys.stdout.write(token)

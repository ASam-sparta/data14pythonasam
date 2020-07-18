import configparser

_config = configparser.ConfigParser()
_config.read('./config.ini') # Handles everything as a dicitonary

def base_url():
    return _config['DEFAULT']['base_url']

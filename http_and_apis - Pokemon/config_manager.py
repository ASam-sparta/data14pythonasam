import configparser

_config = configparser.ConfigParser()
_config.read('./config.ini') # Handles everything as a dictionary


def base_url():
    return _config['DEFAULT']['base_url']

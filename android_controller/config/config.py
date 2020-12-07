import json

config_dc = {}

def get_config():
    global config_dc
    if config_dc != {}:
        return config_dc
    with open("./config.json",'r') as f:
        config_str = f.read()
    config_dc = json.loads(config_str)
    return config_dc
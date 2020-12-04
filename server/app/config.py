
import json

pub_key = ""
pri_key = ""

def get_pub_key():
    global pub_key
    if pub_key != "":
        return pub_key
    pub_key = get_config()["pub_key"]
    return pub_key

def get_pri_key():
    global pri_key
    if pri_key != "":
        return pri_key
    pri_key = get_config()["pri_key"]
    return pri_key

def get_config():
    with open("config.json",'r') as f:
        data = f.read()
    return json.loads(data) 
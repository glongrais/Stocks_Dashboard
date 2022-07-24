import json as js

json_data = None

def load_file(name):
    global json_data
    f = open(name)
    json_data = js.load(f)
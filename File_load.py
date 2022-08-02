import json as js
from Database_operations import add_line

json_data = None

def load_file(name):
    global json_data
    f = open(name)
    json_data = js.load(f)
    for s in json_data:
        add_line(symbol=s['symbol'], quantity=int(s['quantity']),price=float(s['price']),desiredPercentage=float(s['desired_percentage']))
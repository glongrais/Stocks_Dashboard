import json as js
from Database import db, Line

json_data = None

def load_file(name):
    global json_data
    f = open(name)
    json_data = js.load(f)
    for s in json_data:
        l = Line(symbol=s['symbol'], quantity=int(s['quantity']),price=float(s['price']),desired_percent=float(s['desired_percentage']))
        db.session.add(l)
        db.session.commit()
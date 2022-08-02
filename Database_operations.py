from Database import db
from Models import Line, Stock, Transaction, TransactionType
import string
from datetime import datetime

def add_stock(symbol: string, name: string, currentPrice:float, previousClose:float, sector: string, dividendYield:float, logoUrl:string):
    s = Stock(symbol=symbol, name=name, currentPrice=currentPrice, previouslose=previousClose, sector=sector, dividendYield=dividendYield, logoUrl=logoUrl)
    db.session.add(s)
    db.session.commit()

def add_line(symbol: string, price: float, quantity: int, desiredPercentage: float):
    l = Line(symbol=symbol, quantity=quantity, price=price, desiredPercentage=desiredPercentage)
    db.session.add(l)
    db.session.commit()

def add_transaction(date: datetime, type: TransactionType, symbol: string, price: float, quantity: int):
    t = Transaction(date=date, type=type, symbol=symbol, quantity=quantity, price=price)
    db.session.add(t)
    db.session.commit()
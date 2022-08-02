from Database import db
import enum

class TransactionType(enum.Enum):
    SELL = "SELL"
    BUY = "BUY"
    DIVIDEND = "DIVIDEND"

class Stock(db.Model):
    symbol = db.Column(db.String(20), nullable=False, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    currentPrice = db.Column(db.Float, nullable=False)
    previousClose = db.Column(db.Float, nullable=False)
    sector = db.Column(db.String(50), nullable=True)
    dividendYield = db.Column(db.Float, nullable=False)
    logoUrl = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Stock %r>' % self.name

class Line(db.Model):
    symbol = db.Column(db.String(20), nullable=False, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    desiredPercentage = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Line %r>' % self.symbol

class Transaction(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    symbol = db.Column(db.String(50), nullable=False)
    type = db.Column(db.Enum(TransactionType), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Line %r>' % self.symbol
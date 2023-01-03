from app import db

class Card(db.Model):
    card_id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String)
    board = db.relationship("Board", back_populates="cards", lazy=True)
    # an object from the card class can accept a relationship from an object 
    # that's from the Board class. backpopulates signals that the specific board 
    # object will now display this specific card in its board.cards attribute
    board_id = db.Column(db.Integer, db.ForeignKey('board.board_id'), nullable=True)
    likes_count = db.Column(db.Integer)


    
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from ostadtik.Route import prc

__author__ = "NOROUZI"
app = Flask(__name__)
app.register_blueprint(prc)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://scott:root@localhost/OSTADTIK'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = b'\xaelX\x1fI\xa4\xfc{\xb8\x11Zk\xa1\xdb,\xf7L5[Bty\x1c\xb4'
db = SQLAlchemy(app)


class Pricetable(db.Model):
    __table_name__ = "Price"
    pricetableid = db.Column(db.NVARCHAR(50), primary_key=True, unique=True, nullable=True)
    accountostadbank = db.Column(db.NVARCHAR(40), nullable=False)
    classtableid = db.Column(db.NVARCHAR(50), db.ForeignKey('Class.ClassTableID'), nullable=True)
    accountstudent = db.Column(db.NVARCHAR(40), db.ForeignKey('Student.Account'), nullable=False)
    price = db.Column(db.INT, db.ForeignKey('ClassTable.Price'), nullable=True)
    lastnamestudent = db.Column(db.NVARCHAR(40), db.ForeignKey('ClassTable.LastNameStudent'), nullable=True)
    lastnameteacher = db.Column(db.NVARCHAR(40), db.ForeignKey('ClassTable.LastNameTeacher'), nullable=True)


    def __init__(self, accountostadbank):
        self.accountostadbank = accountostadbank

    def __repr__(self):
        return '< PriceTable Table{}'.format(self.__tablename__)

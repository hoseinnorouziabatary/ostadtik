

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from ostadtik.Route import call

__author__ = "NOROUZI"

app = Flask(__name__)
app.register_blueprint(call)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://scott:root@localhost/OSTADTIK'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = b'\xaelX\x1fI\xa4\xfc{\xb8\x11Zk\xa1\xdb,\xf7L5[Bty\x1c\xb4'
db = SQLAlchemy(app)


class Call(db.Model):
    __table_name__ = "Call"
    calltimeid = db.Column(db.NVARCHAR(50), primary_key=True, unique=True, nullable=True)
    azinhour = db.Column(db.NVARCHAR(40), nullable=True)
    tainhour = db.Column(db.NVARCHAR(40), nullable=True)
    azinminutes = db.Column(db.NVARCHAR(40), nullable=True)
    tainminutes = db.Column(db.NVARCHAR(40), nullable=True)
    azinyy = db.Column(db.NVARCHAR(40), nullable=True)
    tainyy = db.Column(db.NVARCHAR(40), nullable=True)
    azinmm = db.Column(db.NVARCHAR(40), nullable=True)
    tainmm = db.Column(db.NVARCHAR(40), nullable=True)
    azindd = db.Column(db.NVARCHAR(40), nullable=True)
    taindd = db.Column(db.NVARCHAR(40), nullable=True)
    teacherid = db.Column(db.NVARCHAR(50), db.ForeignKey('Teacher.TeacherID'), nullable=True)

    def __init__(self, azinhour, tainhour, azinminutes, tainminutes, azinyy, tainyy, azinmm, tainmm, azindd, taindd):
        self.azinhour = azinhour
        self.tainhour = tainhour
        self.azinminutes = azinminutes
        self.tainminutes = tainminutes
        self.azinyy = azinyy
        self.tainyy = tainyy
        self.azinmm = azinmm
        self.tainmm = tainmm
        self.azindd = azindd
        self.taindd = taindd

    def __repr__(self):
        return '<Calltime AzInHour{} TaInHour{} >' .format(self.azinhour, self.tainhour)

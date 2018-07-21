

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from ostadtik.Route import cour


__author__ = "NOROUZI"


app = Flask(__name__)
app.register_blueprint(cour)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://scott:root@localhost/OSTADTIK'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = b'\xaelX\x1fI\xa4\xfc{\xb8\x11Zk\xa1\xdb,\xf7L5[Bty\x1c\xb4'
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Course(db.Model):
    __table_name__ = "Course"
    courseid = db.Column(db.NVARCHAR(50), primary_key=True, unique=True, nullable=True)
    area = db.Column(db.NVARCHAR(40), nullable=True)
    city = db.Column(db.NVARCHAR(40), nullable=True)
    secctionname = db.Column(db.NVARCHAR(40), nullable=True)
    hoursone = db.Column(db.NVARCHAR(40), nullable=True)
    number_count = db.Column(db.NVARCHAR(40), nullable=True)
    price = db.Column(db.INT, nullable=True)
    lastname = db.Column(db.NVARCHAR(40), nullable=True)
    firstname = db.Column(db.NVARCHAR(40), nullable=True)
    count_class = db.Column(db.NVARCHAR(40), nullable=True)
    capacity = db.Column(db.NVARCHAR(40), nullable=True)
    day = db.Column(db.NVARCHAR(40), nullable=True)
    hoursinday = db.Column(db.NVARCHAR(40), nullable=True)
    teacherid = db.Column(db.NVARCHAR(50), db.ForeignKey('Teacher.TeacherID'), nullable=True)

    def __init__(self, area, city, secctionname, hoursone, number_count, price, lastname, firstname, count_class,
                 capacity, day, hoursinday):
        self.area = area
        self.city = city
        self.secctionname = secctionname
        self.hoursone = hoursone
        self.number_count = number_count
        self.price = price
        self.lastname = lastname
        self.firstname = firstname
        self.count_class = count_class
        self.capacity = capacity
        self.day = day
        self.day = hoursinday

    def __repr__(self):
        return '<Course SecctionName{},City{},Area{} >' .format(self.secctionname, self.city, self.area)

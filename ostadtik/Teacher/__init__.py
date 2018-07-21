

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_manager
from ostadtik.Route import Tech

__author__ = "NOROUZI"

app = Flask(__name__)
app.register_blueprint(Tech)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://scott:root@localhost/OSTADTIK'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = b'\xaelX\x1fI\xa4\xfc{\xb8\x11Zk\xa1\xdb,\xf7L5[Bty\x1c\xb4'
db = SQLAlchemy(app)

Login_manager = login_manager
Login_manager.session_protection = "strong"


class Teacher (db.Model, UserMixin):
    __table_name__ = "Teacher"
    teacherid = db.Column(db.NVARCHAR(50), unique=True, primary_key=True, nullable=True)
    educationalrecords = db.Column(db.NVARCHAR(40), nullable=True)
    academichonors = db.Column(db.NVARCHAR(40), nullable=True)
    lastnameteacher = db.Column(db.NVARCHAR(40), nullable=True)
    firstnameteacher = db.Column(db.NVARCHAR(40), nullable=True)
    studentid = db.Column(db.NVARCHAR(40), db.ForeignKey('Student.StudentID'), nullable=True)

    def __init__(self, educationalrecords, academichonors, lastnameteacher, firstnameteacher):
        self.educationalrecords = educationalrecords
        self.academichonors = academichonors
        self.lastnameteacher = lastnameteacher
        self.firstnameteacher = firstnameteacher

    def __repr__(self):
        return '<Teacher LastNameTeacher{} >' .format(self.LastNameTeacher)

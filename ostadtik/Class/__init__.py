from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from ostadtik.Route import clss

__author__ = "NOROUZI"

app = Flask(__name__)
app.register_blueprint(clss)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://scott:root@localhost/OSTADTIK'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = b'\xaelX\x1fI\xa4\xfc{\xb8\x11Zk\xa1\xdb,\xf7L5[Bty\x1c\xb4'
db = SQLAlchemy(app)


class Classtable(db.Model):
    __table_name__ = "ClassTable"
    classtableid = db.Column(db.NVARCHAR(50), primary_key=True, unique=True, nullable=True)
    price = db.Column(db.INT, db.ForeignKey('Course.Price'), nullable=True)
    hoursone = db.Column(db.NVARCHAR(40), db.ForeignKey('Course.HoursOne'), nullable=True)
    number_count = db.Column(db.NVARCHAR(40), db.ForeignKey('Course.NumberCountClass'), nullable=True)
    firstnamestudent = db.Column(db.NVARCHAR(40), db.ForeignKey('Student.FirstNameStudent'), nullable=True)
    firstnameteacher = db.Column(db.NVARCHAR(40), db.ForeignKey('Teacher.FirstNameTeacher'), nullable=True)
    lastnamestudent = db.Column(db.NVARCHAR(40), db.ForeignKey('Student.LastNameStudent'), nullable=True)
    lastnameteacher = db.Column(db.NVARCHAR(40), db.ForeignKey('Teacher.LastNameTeacher'), nullable=True)
    teacherid = db.Column(db.NVARCHAR(50), db.ForeignKey('Teacher.TeacherID'), nullable=True)
    studentid = db.Column(db.NVARCHAR(50), db.ForeignKey('Student.StudentID'), nullable=True)
    courseid = db.Column(db.NVARCHAR(50), db.ForeignKey('Course.CourseID'), nullable=True)
    day = db.Column(db.NVARCHAR(40), db.ForeignKey('Course.Day'), nullable=True)
    hoursinday = db.Column(db.NVARCHAR(40), db.ForeignKey('Course.HoursInDay'), nullable=True)
    temp1 = db.Column(db.BOOLEAN, nullable=True, temp1=False)
    temp2 = db.Column(db.BOOLEAN, nullable=True, temp2=False)

    def __init__(self, price, hoursone, number_count, firstnamestudent, firstnameteacher, lastnamestudent,
                 lastnameteacher, day, hoursinday):
        self.price = price
        self.hoursone = hoursone
        self.number_count = number_count
        self.firstnamestudent = firstnamestudent
        self.firstnameteacher = firstnameteacher
        self.lastnamestudent = lastnamestudent
        self.lastnameteacher = lastnameteacher
        self.day = day
        self.hoursinday = hoursinday

    def __repr__(self):
        return '<Class Day{},HoursInDay{},LastNameStudent{},LastNameTeacher{}>' .format(self.secctionname,
                                                                                        self.hoursinday,
                                                                                        self.lastnamestudent,
                                                                                        self.lastnameteacher)

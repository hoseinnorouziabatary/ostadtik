

from flask_sqlalchemy import SQLAlchemy


__author__ = "NOROUZI"

dcu = SQLAlchemy()


class Course(dcu.Model):
    __table_name__ = "Course"
    courseid = dcu.Column(dcu.NVARCHAR(50), primary_key=True, unique=True, nullable=True)
    area = dcu.Column(dcu.NVARCHAR(40), nullable=True)
    city = dcu.Column(dcu.NVARCHAR(40), nullable=True)
    secctionname = dcu.Column(dcu.NVARCHAR(40), nullable=True)
    hoursone = dcu.Column(dcu.NVARCHAR(40), nullable=True)
    number_count = dcu.Column(dcu.NVARCHAR(40), nullable=True)
    price = dcu.Column(dcu.INT, nullable=True)
    lastname = dcu.Column(dcu.NVARCHAR(40), nullable=True)
    firstname = dcu.Column(dcu.NVARCHAR(40), nullable=True)
    count_class = dcu.Column(dcu.NVARCHAR(40), nullable=True)
    capacity = dcu.Column(dcu.NVARCHAR(40), nullable=True)
    day = dcu.Column(dcu.NVARCHAR(40), nullable=True)
    hoursinday = dcu.Column(dcu.NVARCHAR(40), nullable=True)
    teacherid = dcu.Column(dcu.NVARCHAR(50), dcu.ForeignKey('teacher.TeacherID'), nullable=True)

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
        return '<' \
               'Course SecctionName{},City{},Area{} >' .format(self.secctionname, self.city, self.area)

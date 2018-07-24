

from flask_sqlalchemy import SQLAlchemy


__author__ = "NOROUZI"

dc = SQLAlchemy()


class Course(dc.Model):
    __table_name__ = "Course"
    courseid = dc.Column(dc.NVARCHAR(50), primary_key=True, unique=True, nullable=True)
    area = dc.Column(dc.NVARCHAR(40), nullable=True)
    city = dc.Column(dc.NVARCHAR(40), nullable=True)
    secctionname = dc.Column(dc.NVARCHAR(40), nullable=True)
    hoursone = dc.Column(dc.NVARCHAR(40), nullable=True)
    number_count = dc.Column(dc.NVARCHAR(40), nullable=True)
    price = dc.Column(dc.INT, nullable=True)
    lastname = dc.Column(dc.NVARCHAR(40), nullable=True)
    firstname = dc.Column(dc.NVARCHAR(40), nullable=True)
    count_class = dc.Column(dc.NVARCHAR(40), nullable=True)
    capacity = dc.Column(dc.NVARCHAR(40), nullable=True)
    day = dc.Column(dc.NVARCHAR(40), nullable=True)
    hoursinday = dc.Column(dc.NVARCHAR(40), nullable=True)
    teacherid = dc.Column(dc.NVARCHAR(50), dc.ForeignKey('teacher.TeacherID'), nullable=True)

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

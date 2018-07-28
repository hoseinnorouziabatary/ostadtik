from sqlalchemy import Column, NVARCHAR, ForeignKey, INTEGER

from ostadtik import db

__author__ = "NOROUZI"


class Course(db.Model):
    __table_name__ = "Course"
    courseid = Column(NVARCHAR(50), primary_key=True, unique=True, nullable=True)
    area = Column(NVARCHAR(40), nullable=True)
    city = Column(NVARCHAR(40), nullable=True)
    secctionname = Column(NVARCHAR(40), nullable=True)
    hoursone = Column(NVARCHAR(40), nullable=True)
    number_count = Column(NVARCHAR(40), nullable=True)
    price = Column(INTEGER, nullable=True)
    lastname = Column(NVARCHAR(40), ForeignKey('Student.firstnamestudent'), nullable=True)
    firstname = Column(NVARCHAR(40), ForeignKey('Student.lastnamestudent'), nullable=True)
    count_class = Column(NVARCHAR(40), nullable=True)
    capacity = Column(NVARCHAR(40), nullable=True)
    day = Column(NVARCHAR(40), nullable=True)
    hoursinday = Column(NVARCHAR(40), nullable=True)
    teacherid = Column(NVARCHAR(50), ForeignKey('teacher.TeacherID'), nullable=True)

    def __init__(self, area, city, secctionname, hoursone, number_count, price, count_class,
                 capacity, day, hoursinday):
        self.area = area
        self.city = city
        self.secctionname = secctionname
        self.hoursone = hoursone
        self.number_count = number_count
        self.price = price
        self.count_class = count_class
        self.capacity = capacity
        self.day = day
        self.day = hoursinday

    def __repr__(self):
        return '<' \
               'Course SecctionName{},City{},Area{} >' .format(self.secctionname, self.city, self.area)

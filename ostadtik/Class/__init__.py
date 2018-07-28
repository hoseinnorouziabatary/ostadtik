from sqlalchemy import Column, NVARCHAR, ForeignKey, INTEGER

from ostadtik import db

__author__ = "NOROUZI"


class Classtable(db.Model):
    __table_name__ = "ClassTable"
    classtableid = Column(NVARCHAR(50), primary_key=True, unique=True, nullable=True)
    price = Column(INTEGER, ForeignKey('Course.Price'), nullable=True)
    hoursone = Column(NVARCHAR(40), ForeignKey('Course.HoursOne'), nullable=True)
    number_count = Column(db.NVARCHAR(40), ForeignKey('Course.NumberCountClass'), nullable=True)
    firstnamestudent = Column(db.NVARCHAR(40), ForeignKey('Student.FirstNameStudent'), nullable=True)
    firstnameteacher = Column(db.NVARCHAR(40), ForeignKey('Teacher.FirstNameTeacher'), nullable=True)
    lastnamestudent = Column(db.NVARCHAR(40), ForeignKey('Student.LastNameStudent'), nullable=True)
    lastnameteacher = Column(db.NVARCHAR(40), ForeignKey('Teacher.LastNameTeacher'), nullable=True)
    teacherid = Column(db.NVARCHAR(50), ForeignKey('Teacher.TeacherID'), nullable=True)
    studentid = Column(db.NVARCHAR(50), ForeignKey('Student.StudentID'), nullable=True)
    courseid = Column(db.NVARCHAR(50), ForeignKey('Course.CourseID'), nullable=True)
    day = Column(NVARCHAR(40), ForeignKey('Course.Day'), nullable=True)
    hoursinday = Column(NVARCHAR(40), ForeignKey('Course.HoursInDay'), nullable=True)

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
                                                                                        self.lastnameteacher,
                                                                                        self.point)

from flask_sqlalchemy import SQLAlchemy


__author__ = "NOROUZI"

dcl = SQLAlchemy()


class Classtable(dcl.Model):
    __table_name__ = "ClassTable"
    classtableid = dcl.Column(dcl.NVARCHAR(50), primary_key=True, unique=True, nullable=True)
    price = dcl.Column(dcl.INT, dcl.ForeignKey('course.Price'), nullable=True)
    hoursone = dcl.Column(dcl.NVARCHAR(40), dcl.ForeignKey('course.HoursOne'), nullable=True)
    number_count = dcl.Column(dcl.NVARCHAR(40), dcl.ForeignKey('course.NumberCountClass'), nullable=True)
    firstnamestudent = dcl.Column(dcl.NVARCHAR(40), dcl.ForeignKey('student.FirstNameStudent'), nullable=True)
    firstnameteacher = dcl.Column(dcl.NVARCHAR(40), dcl.ForeignKey('teacher.FirstNameTeacher'), nullable=True)
    lastnamestudent = dcl.Column(dcl.NVARCHAR(40), dcl.ForeignKey('student.LastNameStudent'), nullable=True)
    lastnameteacher = dcl.Column(dcl.NVARCHAR(40), dcl.ForeignKey('teacher.LastNameTeacher'), nullable=True)
    teacherid = dcl.Column(dcl.NVARCHAR(50), dcl.ForeignKey('teacher.TeacherID'), nullable=True)
    studentid = dcl.Column(dcl.NVARCHAR(50), dcl.ForeignKey('student.StudentID'), nullable=True)
    courseid = dcl.Column(dcl.NVARCHAR(50), dcl.ForeignKey('course.CourseID'), nullable=True)
    day = dcl.Column(dcl.NVARCHAR(40), dcl.ForeignKey('course.Day'), nullable=True)
    hoursinday = dcl.Column(dcl.NVARCHAR(40), dcl.ForeignKey('course.HoursInDay'), nullable=True)

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

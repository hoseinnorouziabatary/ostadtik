from sqlalchemy import Column, NVARCHAR, ForeignKey
from flask_login import UserMixin

from ostadtik.route import db

__author__ = "NOROUZI"


class Teacher (db.Model, UserMixin):
    __table_name__ = "teacher"
    teacherid = Column(NVARCHAR(50), unique=True, primary_key=True, nullable=True)
    educationalrecords = Column(NVARCHAR(40), nullable=True)
    academichonors = Column(NVARCHAR(40), nullable=True)
    lastnameteacher = Column(NVARCHAR(40), nullable=True)
    firstnameteacher = Column(NVARCHAR(40), nullable=True)
    studentid = Column(NVARCHAR(40), ForeignKey('student.StudentID'), nullable=True)

    def __init__(self, educationalrecords, academichonors, lastnameteacher, firstnameteacher):
        self.educationalrecords = educationalrecords
        self.academichonors = academichonors
        self.lastnameteacher = lastnameteacher
        self.firstnameteacher = firstnameteacher

    def __repr__(self):
        return '<teacher LastNameTeacher{} >' .format(self.LastNameTeacher)

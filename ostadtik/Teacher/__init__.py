

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_manager


__author__ = "NOROUZI"
dt = SQLAlchemy()
Login_manager = login_manager
Login_manager.session_protection = "strong"


class Teacher (dt.Model, UserMixin):
    __table_name__ = "teacher"
    teacherid = dt.Column(dt.NVARCHAR(50), unique=True, primary_key=True, nullable=True)
    educationalrecords = dt.Column(dt.NVARCHAR(40), nullable=True)
    academichonors = dt.Column(dt.NVARCHAR(40), nullable=True)
    lastnameteacher = dt.Column(dt.NVARCHAR(40), nullable=True)
    firstnameteacher = dt.Column(dt.NVARCHAR(40), nullable=True)
    studentid = dt.Column(dt.NVARCHAR(40), dt.ForeignKey('student.StudentID'), nullable=True)

    def __init__(self, educationalrecords, academichonors, lastnameteacher, firstnameteacher):
        self.educationalrecords = educationalrecords
        self.academichonors = academichonors
        self.lastnameteacher = lastnameteacher
        self.firstnameteacher = firstnameteacher

    def __repr__(self):
        return '<teacher LastNameTeacher{} >' .format(self.LastNameTeacher)

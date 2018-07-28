from sqlalchemy import Column, NVARCHAR
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

from ostadtik import db
from flask import flash

__author__ = "NOROUZI"


class Student(db.Model, UserMixin):
    __table_name__ = "student"
    Studentid = Column(NVARCHAR(50), unique=True, nullable=True, primary_key=True)
    firstnamestudent = Column(NVARCHAR(40), nullable=True)
    lastnamestudent = Column(NVARCHAR(40), nullable=True)
    username = Column(NVARCHAR(40), nullable=True)
    email = Column(NVARCHAR(40), nullable=True)
    passwordstudent = Column(NVARCHAR(40), nullable=True)
    staticphone = Column(NVARCHAR(40), nullable=True)
    dynamicphone = Column(NVARCHAR(40), nullable=True)
    address = Column(NVARCHAR(40), nullable=True)
    sex = Column(NVARCHAR(40), nullable=True)
    accountstudent: Column(NVARCHAR(50), nullable=False)
    flag = Column(NVARCHAR(40), nullable=True)

    def __init__(self, firstnamestudent, lastnamestudent, username, email, passwordstudent, staticphone, accountstudent,
                 dynamicphone, address, sex, flag):
        self.firstnamestudent = firstnamestudent
        self.lastnamestudent = lastnamestudent
        self.username = username
        self.email = email
        self.passwordstudent = passwordstudent
        self.staticphone = staticphone
        self.dynamicphone = dynamicphone
        self.address = address
        self.sex = sex
        self.accountstudent = accountstudent
        self.flag = flag

    def __repr__(self):
        return '<student FirstNameStudent{},LastNameStudent{}>' .format(self.FirstNameStudent, self.LastNameStudent)

    @staticmethod
    def getuserpassword(username):
        return Student.query.filter_by(user=username).first().PasswordStudent

    @property
    def password(self):
        raise AttributeError("Password field is write-only")

    @password.setter
    def password(self, password):
        self.passwordstudent = generate_password_hash(password)
        if len(password) < 8 or len(password) > 50:
            flash('Password must be between 8 and 50 characters')

    def check_password(self, input_password):
        return check_password_hash(self.PasswordStudent, input_password)

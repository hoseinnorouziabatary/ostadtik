

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin, login_manager
from flask import flash

__author__ = "NOROUZI"

dst = SQLAlchemy()
Login_manager = login_manager
Login_manager.session_protection = "strong"


class Student(dst.Model, UserMixin):
    __table_name__ = "student"
    studentid = dst.Column(dst.NVARCHAR(40), unique=True, nullable=True, primary_key=True)
    firstnamestudent = dst.Column(dst.NVARCHAR(40), nullable=True)
    lastnamestudent = dst.Column(dst.NVARCHAR(40), nullable=True)
    username = dst.Column(dst.NVARCHAR(40), nullable=True)
    email = dst.Column(dst.NVARCHAR(40), nullable=True)
    passwordstudent = dst.Column(dst.NVARCHAR(40), nullable=True)
    staticphone = dst.Column(dst.NVARCHAR(40), nullable=True)
    dynamicphone = dst.Column(dst.NVARCHAR(40), nullable=True)
    address = dst.Column(dst.NVARCHAR(40), nullable=True)
    sex = dst.Column(dst.NVARCHAR(40), nullable=True)
    deposited = dst.Column(dst.NVARCHAR(40), nullable=True)
    accountstudent = dst.Column(dst.NVARCHAR(50), nullable=False)
    flag = dst.Column(dst.BOOLEAN, nullable=True)

    def __init__(self, firstnamestudent, lastnamestudent, username, email, passwordstudent, staticphone, accountstudent,
                 dynamicphone, address, sex, deposited, flag):
        self.firstnamestudent = firstnamestudent
        self.lastnamestudent = lastnamestudent
        self.username = username
        self.email = email
        self.passwordstudent = passwordstudent
        self.staticphone = staticphone
        self.dynamicphone = dynamicphone
        self.address = address
        self.sex = sex
        self.deposited = deposited
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



from flask import Flask, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin, login_manager
from ostadtik.Route import stu

__author__ = "NOROUZI"

app = Flask(__name__)
app.register_blueprint(stu)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://scott:root@localhost/OSTADTIK'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = b'\xaelX\x1fI\xa4\xfc{\xb8\x11Zk\xa1\xdb,\xf7L5[Bty\x1c\xb4'
db = SQLAlchemy(app)

Login_manager = login_manager
Login_manager.session_protection = "strong"


class Student(db.Model, UserMixin):
    __table_name__ = "Student"
    studentid = db.Column(db.NVARCHAR(40), unique=True, nullable=True, primary_key=True)
    firstnamestudent = db.Column(db.NVARCHAR(40), nullable=True)
    lastnamestudent = db.Column(db.NVARCHAR(40), nullable=True)
    username = db.Column(db.NVARCHAR(40), nullable=True)
    email = db.Column(db.NVARCHAR(40), nullable=True)
    passwordstudent = db.Column(db.NVARCHAR(40), nullable=True)
    staticphone = db.Column(db.NVARCHAR(40), nullable=True)
    dynamicphone = db.Column(db.NVARCHAR(40), nullable=True)
    address = db.Column(db.NVARCHAR(40), nullable=True)
    sex = db.Column(db.NVARCHAR(40), nullable=True)
    deposited = db.Column(db.NVARCHAR(40), nullable=True)
    accountstudent = db.Column(db.NVARCHAR(50), nullable=False)
    flag = db.Column(db.BOOLEAN, nullable=True, flag=False)

    def __init__(self, firstnamestudent, lastnamestudent, username, email, passwordstudent, staticphone, accountstudent,
                 dynamicphone, address, sex, deposited):
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

    def __repr__(self):
        return '<Student FirstNameStudent{},LastNameStudent{}>' .format(self.FirstNameStudent, self.LastNameStudent)

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

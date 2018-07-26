

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_manager
from ostadtik.Route import pro

__author__ = "NOROUZI"

app = Flask(__name__)
app.register_blueprint(pro)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://scott:root@localhost/OSTADTIK'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = b'\xaelX\x1fI\xa4\xfc{\xb8\x11Zk\xa1\xdb,\xf7L5[Bty\x1c\xb4'
db = SQLAlchemy(app)

Login_manager = login_manager
Login_manager.session_protection = 'strong'


class Profile(db.Model):
    __table_name__ = "Profile"
    profileid = db.Column(db.NVARCHAR(50), unique=True, primary_key=True, nullable=True)
    pdf = db.Column(db.NVARCHAR(40), nullable=True)
    video = db.Column(db.NVARCHAR(40), nullable=True)
    pictuer = db.Column(db.NVARCHAR(40), nullable=True)
    lastname = db.Column(db.NVARCHAR(40), nullable=True)
    firstname = db.Column(db.NVARCHAR(40), nullable=True)
    teacherid = db.Column(db.NVARCHAR(50), db.ForeignKey('Teacher.TeacherID'), nullable=True)
    activenon = db.Column(db.NVARCHAR(40), nullable=True)

    def __init__(self, pdf, video, pictuer, lastname, firstname, activenon):
        self.pdf = pdf
        self.video = video
        self.pictuer = pictuer
        self.lastname = lastname
        self.firstname = firstname
        self.activenon = activenon

    def __repr__(self):
        return '<Profile LastName{},FirstName{} >' .format(self.lastname, self.firstname)

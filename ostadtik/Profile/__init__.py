

from flask_sqlalchemy import SQLAlchemy
from flask_login import login_manager

__author__ = "NOROUZI"

dp = SQLAlchemy()
Login_manager = login_manager
Login_manager.session_protection = 'strong'


class Profile(dp.Model):
    __table_name__ = "profile"
    profileid = dp.Column(dp.NVARCHAR(50), unique=True, primary_key=True, nullable=True)
    pdf = dp.Column(dp.NVARCHAR(40), nullable=True)
    video = dp.Column(dp.NVARCHAR(40), nullable=True)
    pictuer = dp.Column(dp.NVARCHAR(40), nullable=True)
    lastname = dp.Column(dp.NVARCHAR(40), nullable=True)
    firstname = dp.Column(dp.NVARCHAR(40), nullable=True)
    teacherid = dp.Column(dp.NVARCHAR(50), dp.ForeignKey('teacher.TeacherID'), nullable=True)
    activenon = dp.Column(dp.NVARCHAR(40), nullable=True)

    def __init__(self, pdf, video, pictuer, lastname, firstname, activenon):
        self.pdf = pdf
        self.video = video
        self.pictuer = pictuer
        self.lastname = lastname
        self.firstname = firstname
        self.activenon = activenon

    def __repr__(self):
        return '<profile LastName{},FirstName{} >' .format(self.lastname, self.firstname)

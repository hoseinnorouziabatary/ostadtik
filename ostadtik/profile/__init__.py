from sqlalchemy import Column, NVARCHAR, ForeignKey

from ostadtik import db

__author__ = "NOROUZI"


class Profile(db.Model):
    __table_name__ = "profile"
    profileid = Column(NVARCHAR(50), unique=True, primary_key=True, nullable=True)
    pdf = Column(NVARCHAR(40), nullable=True)
    video = Column(NVARCHAR(40), nullable=True)
    pictuer = Column(NVARCHAR(40), nullable=True)
    lastname = Column(NVARCHAR(40), nullable=True)
    firstname = Column(NVARCHAR(40), nullable=True)
    teacherid = Column(NVARCHAR(50), ForeignKey('teacher.TeacherID'), nullable=True)
    activenon = Column(NVARCHAR(40), nullable=True)

    def __init__(self, pdf, video, pictuer, lastname, firstname, activenon):
        self.pdf = pdf
        self.video = video
        self.pictuer = pictuer
        self.lastname = lastname
        self.firstname = firstname
        self.activenon = activenon

    def __repr__(self):
        return '<profile LastName{},FirstName{} >' .format(self.lastname, self.firstname)

from sqlalchemy import Column, NVARCHAR, ForeignKey

from ostadtik import db

__author__ = "NOROUZI"


class Profile(db.Model):
    __table_name__ = "profile"
    profileid = Column(NVARCHAR(50), unique=True, primary_key=True, nullable=True)
    pdf = Column(NVARCHAR(40), nullable=True)
    video = Column(NVARCHAR(40), nullable=True)
    pictuer = Column(NVARCHAR(40), nullable=True)
    lastnameteacher = Column(NVARCHAR(40), ForeignKey('Teacher.lastnameteacher'), nullable=True)
    firstnameteacher = Column(NVARCHAR(40), ForeignKey('Teacher.firstnameteacher'), nullable=True)
    teacherid = Column(NVARCHAR(50), ForeignKey('teacher.TeacherID'), nullable=True)
    activenon = Column(NVARCHAR(40), nullable=True)

    def __init__(self, pdf, video, pictuer, activenon):
        self.pdf = pdf
        self.video = video
        self.pictuer = pictuer
        self.activenon = activenon

    def __repr__(self):
        return '<profile LastName{},FirstName{} >' .format(self.lastname, self.firstname)

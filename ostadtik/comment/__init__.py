from sqlalchemy import Column, NVARCHAR

from ostadtik import db

__author__ = "NOROUZI"


class Comment(db.Model):
    __table_name__ = "Comment"
    commentid = Column(NVARCHAR(50), primary_key=True, unique=True, nullable=True)
    firstnameteachercomment = Column(NVARCHAR(40), nullable=True)
    lastnameteachercomment = Column(NVARCHAR(40), nullable=True)
    usernamecomment = Column(NVARCHAR(40), nullable=True)
    commandtext = Column(NVARCHAR(40), nullable=True)

    def __init__(self, firstnameteachercomment, lastnameteachercomment, usernamecomment, commandtext):
        self.firstnameteachercomment = firstnameteachercomment
        self.lastnameteachercomment = lastnameteachercomment
        self.usernamecomment = usernamecomment
        self.commandtext = commandtext

    def __repr__(self):
        return '<Comment firstnameteachercomment{},lastnameteachercomment{},usernamecomment{}>'.format(
            self.firstnameteachercomment, self.lastnameteachercomment, self.usernamecomment)

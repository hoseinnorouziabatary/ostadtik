from sqlalchemy import Column, NVARCHAR, ForeignKey, INTEGER

from ostadtik import db

__author__ = "NOROUZI"


class Comment(db.Model):
    __table_name__ = "Comment"
    commentid = Column(NVARCHAR(50), primary_key=True, unique=True, nullable=True)
    comment_text = Column(NVARCHAR(1000), nullable=True)
    point = Column(INTEGER, nullable=True)
    reply_text = Column(NVARCHAR(1000), nullable=True)
    classtableid = Column(NVARCHAR(50), ForeignKey('ClassTable.ClassTableID'), nullable=True)
    firstnameteacher = Column(NVARCHAR(40), ForeignKey('teacher.FirstNameTeacher'), nullable=True)
    lastnameteacher = Column(NVARCHAR(40), ForeignKey('teacher.LastNameTeacher'), nullable=True)
    firstnamestudent = Column(NVARCHAR(40), ForeignKey('student.FirstNameStudent'), nullable=True)
    lastnamestudent = Column(NVARCHAR(40), ForeignKey('student.LastNameStudent'), nullable=True)

    def __init__(self, comment_text, point, reply_text):
        self.comment_text = comment_text
        self.point = point
        self.reply_text = reply_text

    def __repr__(self):
        return '<Comment Commenttext{},Point{},Replytext{} ,LastNameTeacher{},LastNameStudent{}>' .format(
            self.Comment_text, self.Point, self.Replytext, self.LastNameTeacher, self.LastNameStudent)

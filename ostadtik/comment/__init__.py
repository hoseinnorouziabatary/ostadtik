
from flask_sqlalchemy import SQLAlchemy


__author__ = "NOROUZI"

dcm = SQLAlchemy()


class Comment(dcm.Model):
    __table_name__ = "Comment"
    commentid = dcm.Column(dcm.NVARCHAR(50), primary_key=True, unique=True, nullable=True)
    comment_text = dcm.Column(dcm.NVARCHAR(1000), nullable=True)
    point = dcm.Column(dcm.INT, nullable=True)
    reply_text = dcm.Column(dcm.NVARCHAR(1000), nullable=True)
    classtableid = dcm.Column(dcm.NVARCHAR(50), dcm.ForeignKey('ClassTable.ClassTableID'), nullable=True)
    firstnameteacher = dcm.Column(dcm.NVARCHAR(40), dcm.ForeignKey('teacher.FirstNameTeacher'), nullable=True)
    lastnameteacher = dcm.Column(dcm.NVARCHAR(40), dcm.ForeignKey('teacher.LastNameTeacher'), nullable=True)
    firstnamestudent = dcm.Column(dcm.NVARCHAR(40), dcm.ForeignKey('student.FirstNameStudent'), nullable=True)
    lastnamestudent = dcm.Column(dcm.NVARCHAR(40), dcm.ForeignKey('student.LastNameStudent'), nullable=True)

    def __init__(self, comment_text, point, reply_text):
        self.comment_text = comment_text
        self.point = point
        self.reply_text = reply_text

    def __repr__(self):
        return '<Comment Commenttext{},Point{},Replytext{} ,LastNameTeacher{},LastNameStudent{}>' .format(
            self.Comment_text, self.Point, self.Replytext, self.LastNameTeacher, self.LastNameStudent)

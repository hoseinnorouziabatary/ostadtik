

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from ostadtik.Route import cmt


__author__ = "NOROUZI"


app = Flask(__name__)
app.register_blueprint(cmt)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://scott:root@localhost/OSTADTIK'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = b'\xaelX\x1fI\xa4\xfc{\xb8\x11Zk\xa1\xdb,\xf7L5[Bty\x1c\xb4'
db = SQLAlchemy(app)


class Comment(db.Model):
    __table_name__ = "Comment"
    commentid = db.Column(db.NVARCHAR(50), primary_key=True, unique=True, nullable=True)
    comment_text = db.Column(db.NVARCHAR(1000), nullable=True)
    point = db.Column(db.INT, nullable=True)
    reply_text = db.Column(db.NVARCHAR(1000), nullable=True)
    classtableid = db.Column(db.NVARCHAR(50), db.ForeignKey('ClassTable.ClassTableID'), nullable=True)
    firstnameteacher = db.Column(db.NVARCHAR(40), db.ForeignKey('Teacher.FirstNameTeacher'), nullable=True)
    lastnameteacher = db.Column(db.NVARCHAR(40), db.ForeignKey('Teacher.LastNameTeacher'), nullable=True)
    firstnamestudent = db.Column(db.NVARCHAR(40), db.ForeignKey('Student.FirstNameStudent'), nullable=True)
    lastnamestudent = db.Column(db.NVARCHAR(40), db.ForeignKey('Student.LastNameStudent'), nullable=True)

    def __init__(self, comment_text, point, reply_text):
        self.comment_text = comment_text
        self.point = point
        self.reply_text = reply_text

    def __repr__(self):
        return '<Comment Commenttext{},Point{},Replytext{} ,LastNameTeacher{},LastNameStudent{}>' .format(
            self.Comment_text, self.Point, self.Replytext, self.LastNameTeacher, self.LastNameStudent)

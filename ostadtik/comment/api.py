from flask import Blueprint, request, jsonify, flash

from ostadtik.route import db
from ostadtik.comment import Comment

__author__ = "NOROUZI"

comment = Blueprint("comment", __name__)


@comment.route('/comment', methods=['GET', 'POST'])
def comment():
    comment_text = request.json['']
    point = request.json['']
    reply_text = request.json['']

    db.session.add(Comment(comment_text=comment_text, point=point, reply_text=reply_text))
    db.session.commit()

    flash("The operation was successful")
    return jsonify('')

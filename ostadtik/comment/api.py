from flask import Blueprint, request, jsonify

from ostadtik import db
from ostadtik.comment import Comment

__author__ = "NOROUZI"

comment_blueprint = Blueprint("comment", __name__)


@comment_blueprint.route('/comment', methods=['GET', 'POST'])
def comment_route():
    firstnameteachercomment = request.json['FirstNameTeacherComment']
    lastnameteachercomment = request.json['LastNameTeacherComment']
    usernamecomment = request.json['UserNameComment']
    commandtext = request.json['CommandText']

    db.session.add(Comment(firstnameteachercomment=firstnameteachercomment,
                           lastnameteachercomment=lastnameteachercomment,
                           usernamecomment=usernamecomment, commandtext=commandtext))
    db.session.commit()

    return jsonify({"Firstnameteachercomment": firstnameteachercomment,
                    "Lastnameteachercomment": lastnameteachercomment, "usernamecomment": usernamecomment,
                    "commandtext": commandtext})

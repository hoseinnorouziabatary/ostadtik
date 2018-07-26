from flask import Blueprint, request, flash, jsonify

from ostadtik import db
from ostadtik.teacher import Teacher
from ostadtik.Student import Student


__author__ = "NOROUZI"

teacher = Blueprint("teacher", __name__)


@teacher.route('/register_teacher', methods=["GET", "POST"])
def register_teacher():
    educationalrecords = request.json['']
    academichonors = request.json['']
    lastnameteacher = request.json['']
    firstnameteacher = request.json['']

    Student.i.query.filter_by(Student.flag).Update(flag=True)

    db.session.add(Teacher(educationalrecords=educationalrecords, academichonors=academichonors,
                           lastnameteacher=lastnameteacher, firstnameteacher=firstnameteacher, ))
    db.session.commit()

    flash("User registered successfully !")
    return jsonify('hello')

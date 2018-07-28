from flask import Blueprint, request, flash, jsonify

from ostadtik import db
from ostadtik.teacher import Teacher
from ostadtik.Student import Student


__author__ = "NOROUZI"

teacher = Blueprint("teacher", __name__)


@teacher.route('/register_teacher', methods=["GET"])
def register_teacher():
    educationalrecords = request.json['']
    academichonors = request.json['']
    lastnameteacher = request.json['']
    firstnameteacher = request.json['']
    flag = request.json['']

    Student.i.query.filter_by(Student.flag).Update(flag=flag)

    db.session.add(Teacher(educationalrecords=educationalrecords, academichonors=academichonors,
                           lastnameteacher=lastnameteacher, firstnameteacher=firstnameteacher, ))
    db.session.commit()
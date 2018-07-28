from flask import Blueprint, request

from ostadtik import db
from ostadtik.teacher import Teacher
from ostadtik.Student import Student


__author__ = "NOROUZI"

teacher = Blueprint("teacher", __name__)


@teacher.route('/register_teacher', methods=["GET"])
def register_teacher():
    educationalrecords = request.json['educationalrecords']
    academichonors = request.json['academichonors']
    flag = request.json['Flag']

    Student.i.query.filter_by(Student.flag).Update(flag=flag)
    db.session.add(Teacher(educationalrecords=educationalrecords, academichonors=academichonors))
    db.session.commit()

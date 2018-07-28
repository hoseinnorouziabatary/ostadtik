from flask import Blueprint, request

from ostadtik import db
from ostadtik.course import Course


__author__ = "NOROUZI"

course = Blueprint("course", __name__)


@course.route('/course', methods=['GET'])
def course_route():
    area = request.json['']
    city = request.json['']
    secctionname = request.json['']
    hoursone = request.json['']
    numbercount = request.json['']
    price = request.json['']
    lastname = request.json['']
    firstname = request.json['']
    countclass = request.json['']
    capacity = request.json['']
    day = request.json['']
    hoursinday = request.json['']

    db.session.add(Course(area=area, city=city, secctionname=secctionname, hoursone=hoursone, number_count=numbercount,
                          price=price, lastname=lastname, firstname=firstname,
                          count_class=countclass, capacity=capacity, day=day, hoursinday=hoursinday))
    db.session.commit()

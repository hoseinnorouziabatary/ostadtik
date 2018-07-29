from flask import Blueprint, request, jsonify

from ostadtik import db
from ostadtik.course import Course


__author__ = "NOROUZI"

course = Blueprint("course", __name__)


@course.route('/course', methods=['GET'])
def course_route():
    area = request.json['Area']
    city = request.json['City']
    secctionname = request.json['SecctionName']
    hoursone = request.json['HoursOneClass']
    numbercount = request.json['NumberCount']
    price = request.json['Price']
    countclass = request.json['ClassCount']
    capacity = request.json['Capacity']
    day = request.json['Day']
    hoursinday = request.json['HoursinDay']

    db.session.add(Course(area=area, city=city, secctionname=secctionname, hoursone=hoursone, number_count=numbercount,
                          price=price,
                          count_class=countclass, capacity=capacity, day=day, hoursinday=hoursinday))
    db.session.commit()

    return jsonify({"Area": area, "city": city, "secctionname": secctionname, "hoursone": hoursone,
                    "numbercount": numbercount, "price": price, "countclass": countclass, "capacity": capacity,
                    "day": day, "hoursinday": hoursinday})

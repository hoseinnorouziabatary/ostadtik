from flask import Blueprint, request, jsonify, flash

from ostadtik.route import db
from ostadtik.price import Pricetable
from ostadtik.course import Course
from ostadtik.Student import Student

__author__ = "NOROUZI"

price = Blueprint("price", __name__)


@price.route('/Class/transaction')
def transaction():
    if Course.price <= Student.accountstudent:
        trans = Course.price - Student.accountstudent.where(Pricetable.lastnamestudent == Student.lastnamestudent)
        Student.query.filter_by(Student.accountstudent).Update(accountstudent=trans)
        Pricetable.query.filter_by(Pricetable.accountostadbank).Update(accountostadbank=Course)
        db.session.commit()
    return flash("Inventory is not enough")


from flask import Blueprint, flash

from ostadtik import db
from ostadtik.price import Pricetable
from ostadtik.course import Course
from ostadtik.Student import Student

__author__ = "NOROUZI"

price = Blueprint("price", __name__)


@price.route('/Class/transaction')
def transaction():
    accont_student = Student.accountstudent
    if Course.price <= accont_student:
        trans = Course.price - Student.accountstudent.where(Pricetable.lastnamestudent == Student.lastnamestudent)
        Student.query.filter_by(Student.accountstudent).Update(accountstudent=trans)
        Pricetable.query.filter_by(Pricetable.accountostadbank).Update(accountostadbank=Course)
        db.session.commit()
    return flash("Inventory is not enough")


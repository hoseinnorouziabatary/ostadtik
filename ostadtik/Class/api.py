from flask import Blueprint, jsonify, request


from ostadtik import db
from ostadtik.Student import Student
from ostadtik.price import Pricetable
from ostadtik.Class import Classtable
__author__ = "NOROUZI"

classtable = Blueprint("classtable", __name__)


@classtable.route('/class', methods=['GET', 'POST'])
def get_class():
    data = Classtable.query.all()

    data_all = []

    for counts in data:
        data_all.append([counts.classtableid, counts.price, counts.hoursone, counts.numbercountclass,
                         counts.firstnamestudent, counts.firstnameteacher, counts.lastnamestudent,
                         counts.lastnameteacher, counts.day, counts.hoursinday])

    return jsonify(ClassTable=data_all)


@classtable.route('/Class/payment', methods=['GET','POST'])
def payment():

    if Classtable.price <= Pricetable.ostadbank:
        sub = Classtable.price - Pricetable.ostadbank
        summ = Student.accountstudent + Classtable.price
        Student.query.filter_by(Student.accountstudent).Update(accountstudent=summ)
        Pricetable.query.filter_by(Pricetable.accountostadbank).Update(accountostadbank=sub)
        db.session.commit()

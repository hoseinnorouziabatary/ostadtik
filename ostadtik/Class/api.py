from flask import Blueprint, jsonify,request


from ostadtik import db
from ostadtik.Student import Student
from ostadtik.price import Pricetable
from ostadtik.Class import Classtable
from ostadtik.course import Course

__author__ = "NOROUZI"

classtable = Blueprint("classtable", __name__)


@classtable.route('/class', methods=['GET', 'POST'])
def get_class():

    data = Classtable.query.all()

    data_all = []

    for counts in data:
        data_all.append([counts.price, counts.hoursone, counts.numbercountclass,
                         counts.firstnamestudent, counts.firstnameteacher, counts.lastnamestudent,
                         counts.lastnameteacher, counts.day, counts.hoursinday])

    return jsonify({"ClassTable": data_all})


@classtable.route('/Class/prepayment', methods=['GET', 'POST'])
def payment():
    true = request.json['Prepayment']
    temp = 'ok'
    if temp == true:
        if Classtable.price <= Pricetable.ostadbank:
            sub = Classtable.price - Pricetable.ostadbank
            summ = Student.accountstudent + Classtable.price
            Student.query.filter_by(Student.accountstudent).Update(accountstudent=summ)
            Pricetable.query.filter_by(Pricetable.accountostadbank).Update(accountostadbank=sub)
            db.session.commit()
    return jsonify({"ok": temp})


@classtable.route('/Class/transaction', methods=['GET', 'POST'])
def transaction():
    flag_student = request.json['SubmitStudent']
    flag_teacher = request.json['SubmitTeacher']
    if flag_student == flag_teacher:
        accont_student = Student.accountstudent
        if Course.price <= accont_student:
            trans = Course.price - Student.accountstudent.where(
                Pricetable.lastnamestudent == Student.lastnamestudent)
            Student.query.filter_by(Student.accountstudent).Update(accountstudent=trans)
            Pricetable.query.filter_by(Pricetable.accountostadbank).Update(accountostadbank=Course)
            db.session.commit()
        return jsonify("Inventory is not enough")

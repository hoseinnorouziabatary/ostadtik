

from ..Calltime import db, Call
from ..comment import db, Comment
from ..Course import db, Course
from ..Student import db, Student
from ..Teacher import db, Teacher
from ..Profile import db
from ..Class import db, Classtable
from ..price import db, Pricetable
from flask import Blueprint, request, jsonify, flash
from flask_login import login_user, logout_user


__author__ = "NOROUZI"

call = Blueprint("Calltime", __name__)
cmt = Blueprint("comment", __name__)
cour = Blueprint("Course", __name__)
stu = Blueprint("Student", __name__)
Tech = Blueprint("Teacher", __name__)
pro = Blueprint("Profile", __name__)
clss = Blueprint("Profile", __name__)
prc = Blueprint("price", __name__)


@call.route('/Call', methods=['POST'])
def call():
    azinhour = request.json['']
    tainhour = request.json['']
    azinminutes = request.json['']
    tainminutes = request.json['']
    azinyy = request.json['']
    tainyy = request.json['']
    azinmm = request.json['']
    tainmm = request.json['']
    azindd = request.json['']
    taindd = request.json['']

    db.session.add(Call(azinhour=azinhour, tainhour=tainhour, azinminutes=azinminutes, tainminutes=tainminutes,
                        azinyy=azinyy, tainyy=tainyy, azinmm=azinmm, tainmm=tainmm, azindd=azindd, taindd=taindd))
    db.session.commit()

    flash("The operation was successful")
    return jsonify('')


@cmt.route('/Comment', methods=['GET'])
def comment():
    comment_text = request.json['']
    point = request.json['']
    reply_text = request.json['']

    db.session.add(Comment(comment_text=comment_text, point=point, reply_text=reply_text))
    db.session.commit()

    flash("The operation was successful")
    return jsonify('')


@cour.route('/Course', methods=['POST'])
def course():

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


@stu.route('/register', methods=["GET", "POST"])
def register():
        firstname = request.json['']
        username = request.json['']
        password = request.json['']
        rewritepassword = request.json['']
        lastname = request.json['']
        email = request.json['']
        staticphone = request.json['']
        dynamicphone = request.json['']
        address = request.json['']
        sex = request.json['']
        depositedy = request.json['']

        if rewritepassword == password:
            db.session.add(Student(username=username, passwordstudent=password,
                                   firstnamestudent=firstname, lastnamestudent=lastname, email=email,
                                   staticphone=staticphone, dynamicphone=dynamicphone, address=address, sex=sex,
                                   deposited=depositedy, accountstudent=0))

            db.session.commit()

        flash("User registered successfully !")
        return jsonify('hello')


@stu.route('/login', methods=["GET"])
def login():
    username = request.json['']
    password = request.json['']

    stored_user = Student.query.filter_by(username=username).first()
    if stored_user is not None and stored_user.check_password(password):
        login_user(stored_user)
        flash("you are logged as {} to your account.".format(stored_user.user))
        return jsonify('')
    else:
        flash("user or password is incorrect")
        return jsonify('')


@stu.route('/logout')
def logout():
    logout_user()
    flash('you are logged out successfully !')
    return jsonify('')


@stu.route('/update')
def update():
    updateaccont = request.json[""]

    Student.query.filter_by(Student.accountstudent).Update(accountstudent=updateaccont)
    db.session.commit()


@Tech.route('/registerTeacher', methods=["GET", "POST"])
def register_teacher():
    educationalrecords = request.json['']
    academichonors = request.json['']
    lastnameteacher = request.json['']
    firstnameteacher = request.json['']

    Student.query.filter_by(Student.flag).Update(flag=True)

    db.session.add(Teacher(educationalrecords=educationalrecords, academichonors=academichonors,
                           lastnameteacher=lastnameteacher, firstnameteacher=firstnameteacher,))
    db.session.commit()

    flash("User registered successfully !")
    return jsonify('hello')


@clss.route('/Class', methods=['GET', 'POST'])
def get_class():

    data = Classtable.query.all()

    data_all = []

    for counts in data:
        data_all.append([counts.classtableid, counts.price, counts.hoursone, counts.numbercountclass,
                         counts.firstnamestudent, counts.firstnameteacher, counts.lastnamestudent,
                         counts.lastnameteacher, counts.day, counts.hoursinday])

    return jsonify(ClassTable=data_all)


if Course.price <= Pricetable.accountostadbank:
    sub = Course.price - Pricetable.accountostadbank
    Total = Student.accountstudent + Course.price
    Student.query.filter_by(Student.accountstudent).Update(accountstudent=Total)
    Pricetable.query.filter_by(Pricetable.accountostadbank).Update(accountostadbank=sub)
    db.session.commit()


@clss.route("/Class/transaction", methods=['GET'])
def transaction():
    if Course.price <= Student.accountstudent:
        trans = Course.price - Student.accountstudent.Where(Pricetable.lastnamestudent == Student.lastnamestudent)
        Student.query.filter_by(Student.accountstudent).Update(accountstudent=trans)
        Pricetable.query.filter_by(Pricetable.accountostadbank).Update(accountostadbank=Course.price)
        db.session.commit()
    return flash("Inventory is not enough")



from flask import Blueprint, request, jsonify, flash
from flask_login import login_user, logout_user
from ostadtik.Calltime import Call, dv
from ostadtik.comment import Comment, db
from ostadtik.Course import Course, dc
from ostadtik.Student import Student, dst
from ostadtik.Teacher import Teacher, dt
from ostadtik.Profile import Profile, dp
from ostadtik.Class import Classtable, dcl
from ostadtik.price import Pricetable, dpr


__author__ = "NOROUZI"

cal = Blueprint("Calltime", __name__)
cmt = Blueprint("comment", __name__)
cour = Blueprint("Course", __name__)
stu = Blueprint("student", __name__)
Tech = Blueprint("teacher", __name__)
pro = Blueprint("profile", __name__)
clss = Blueprint("profile", __name__)
prc = Blueprint("price", __name__)


@cal.route('/Call', methods=['POST'])
def cal():
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

    dv.session.add(Call(azinhour=azinhour, tainhour=tainhour, azinminutes=azinminutes, tainminutes=tainminutes,
                        azinyy=azinyy, tainyy=tainyy, azinmm=azinmm, tainmm=tainmm, azindd=azindd, taindd=taindd))
    dv.session.commit()

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

    dc.session.add(Course(area=area, city=city, secctionname=secctionname, hoursone=hoursone, number_count=numbercount,
                          price=price, lastname=lastname, firstname=firstname,
                          count_class=countclass, capacity=capacity, day=day, hoursinday=hoursinday))
    dc.session.commit()


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
            dst.session.add(Student(username=username, passwordstudent=password, firstnamestudent=firstname,
                                    lastnamestudent=lastname, email=email,  staticphone=staticphone,
                                    dynamicphone=dynamicphone, address=address, sex=sex, deposited=depositedy,
                                    accountstudent=0, flag=False))

            dst.session.commit()

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
    dst.session.commit()


@pro.route('/register_profile', method=["POST"])
def registerprofile():
    pdf = request.json['']
    video = request.json['']
    pictuer = request.json['']
    lastname = request.json['']
    firstname = request.json['']
    activenon = request.json['']

    dp.session.add(Profile(pdf=pdf, video=video, pictuer=pictuer, lastname=lastname, firstname=firstname,
                           activenon=activenon))


@Tech.route('/registerTeacher', methods=["GET", "POST"])
def register_teacher():
    educationalrecords = request.json['']
    academichonors = request.json['']
    lastnameteacher = request.json['']
    firstnameteacher = request.json['']

    Student.query.filter_by(Student.flag).Update(flag=True)

    dt.session.add(Teacher(educationalrecords=educationalrecords, academichonors=academichonors,
                           lastnameteacher=lastnameteacher, firstnameteacher=firstnameteacher,))
    dt.session.commit()

    flash("User registered successfully !")
    return jsonify('hello')


@cls.route('/Class', methods=['GET', 'POST'])
def get_class():

    data = Classtable.query.all()

    data_all = []

    for counts in data:
        data_all.append([counts.classtableid, counts.price, counts.hoursone, counts.numbercountclass,
                         counts.firstnamestudent, counts.firstnameteacher, counts.lastnamestudent,
                         counts.lastnameteacher, counts.day, counts.hoursinday])

    return jsonify(ClassTable=data_all)


@cls.route("/Class/payment")
def payment():
    if Classtable.price <= Pricetable.accountostadbank:
        sub = Classtable.price - Pricetable.accountostadbank
        summ = Student.accountstudent + Classtable.price
        Student.query.filter_by(Student.accountstudent).Update(accountstudent=summ)
        Pricetable.query.filter_by(Pricetable.accountostadbank).Update(accountostadbank=sub)
        dcl.session.commit()


@prc.route("/Class/payment/transaction", methods=['GET'])
def transaction():
    if course.price <= Student.accountstudent:
        trans = course.price - Student.accountstudent.Where(Pricetable.lastnamestudent == Student.lastnamestudent)
        Student.query.filter_by(Student.accountstudent).Update(accountstudent=trans)
        Pricetable.query.filter_by(Pricetable.accountostadbank).Update(accountostadbank=course.price)
        dpr.session.commit()
    return flash("Inventory is not enough")

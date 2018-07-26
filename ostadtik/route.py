#from flask_login import login_user, logout_user
from flask_sqlalchemy import SQLAlchemy

# from ostadtik.Calltime import Call, dcl
# from ostadtik.comment import Comment, dcm
# from ostadtik.course import Course, dcu
# from ostadtik.student import Student, dst
# from ostadtik.teacher import Teacher, dte
# from ostadtik.Class import Classtable, dcls
# from ostadtik.price import Pricetable, dpri

__author__ = "NOROUZI"


db = SQLAlchemy()


def create_app(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # app.register_blueprint(calltime_dv)
    # app.register_blueprint(comment_db)
    # app.register_blueprint(course_dc)
    from ostadtik.Student import student as student_blueprint
    app.register_blueprint(student_blueprint)
    from ostadtik.teacher.api import teacher as teacher_blueprint
    app.register_blueprint(teacher_blueprint)
    from ostadtik.profile.api import profile as profile_blueprint
    app.register_blueprint(profile_blueprint)
    # app.register_blueprint(classtable_dcl)
    # app.register_blueprint(pricetable_dpr)

    return app


# cal = Blueprint("Calltime", __name__)
# cmt = Blueprint("comment", __name__)
# cour = Blueprint("Course", __name__)
# stu = Blueprint("student", __name__)
# tech = Blueprint("teacher", __name__)
# clss = Blueprint("profile", __name__)
# prc = Blueprint("price", __name__)
#
#
# @cal.route('/Call', methods=['POST'])
# def cal():
#     azinhour = request.json['']
#     tainhour = request.json['']
#     azinminutes = request.json['']
#     tainminutes = request.json['']
#     azinyy = request.json['']
#     tainyy = request.json['']
#     azinmm = request.json['']
#     tainmm = request.json['']
#     azindd = request.json['']
#     taindd = request.json['']
#
#     dcl.session.add(Call(azinhour=azinhour, tainhour=tainhour, azinminutes=azinminutes, tainminutes=tainminutes,
#                          azinyy=azinyy, tainyy=tainyy, azinmm=azinmm, tainmm=tainmm, azindd=azindd, taindd=taindd))
#     dcl.session.commit()
#
#     flash("The operation was successful")
#     return jsonify('')
#
#
# @cmt.route('/Comment', methods=['GET'])
# def comment():
#     comment_text = request.json['']
#     point = request.json['']
#     reply_text = request.json['']
#
#     dcm.session.add(Comment(comment_text=comment_text, point=point, reply_text=reply_text))
#     dcm.session.commit()
#
#     flash("The operation was successful")
#     return jsonify('')
#
#
# @cour.route('/Course', methods=['POST'])
# def course():
#
#     area = request.json['']
#     city = request.json['']
#     secctionname = request.json['']
#     hoursone = request.json['']
#     numbercount = request.json['']
#     price = request.json['']
#     lastname = request.json['']
#     firstname = request.json['']
#     countclass = request.json['']
#     capacity = request.json['']
#     day = request.json['']
#     hoursinday = request.json['']
#
#     dcu.session.add(Course(area=area, city=city, secctionname=secctionname, hoursone=hoursone, number_count=numbercount,
#                            price=price, lastname=lastname, firstname=firstname,
#                            count_class=countclass, capacity=capacity, day=day, hoursinday=hoursinday))
#     dcu.session.commit()
#



#
#
# @techer.route('/registerTeacher', methods=["GET", "POST"])
# def register_teacher():
#     educationalrecords = request.json['']
#     academichonors = request.json['']
#     lastnameteacher = request.json['']
#     firstnameteacher = request.json['']
#
#     Student.query.filter_by(Student.flag).Update(flag=True)
#
#     dte.session.add(Teacher(educationalrecords=educationalrecords, academichonors=academichonors,
#                             lastnameteacher=lastnameteacher, firstnameteacher=firstnameteacher,))
#     dte.session.commit()
#
#     flash("User registered successfully !")
#     return jsonify('hello')
#
#
# @clss.route('/Class', methods=['GET', 'POST'])
# def get_class():
#
#     data = Classtable.query.all()
#
#     data_all = []
#
#     for counts in data:
#         data_all.append([counts.classtableid, counts.price, counts.hoursone, counts.numbercountclass,
#                          counts.firstnamestudent, counts.firstnameteacher, counts.lastnamestudent,
#                          counts.lastnameteacher, counts.day, counts.hoursinday])
#
#     return jsonify(ClassTable=data_all)
#
#
# @clss.route("/Class/payment")
# def payment():
#     if Classtable.price <= Pricetable.accountostadbank:
#         sub = Classtable.price - Pricetable.accountostadbank
#         summ = Student.accountstudent + Classtable.price
#         Student.query.filter_by(Student.accountstudent).Update(accountstudent=summ)
#         Pricetable.query.filter_by(Pricetable.accountostadbank).Update(accountostadbank=sub)
#         dcls.session.commit()
#
#
# @prc.route("/Class/payment/transaction", methods=['GET'])
# def transaction():
#     if course.price <= Student.accountstudent:
#         trans = course.price - Student.accountstudent.Where(Pricetable.lastnamestudent == Student.lastnamestudent)
#         Student.query.filter_by(Student.accountstudent).Update(accountstudent=trans)
#         Pricetable.query.filter_by(Pricetable.accountostadbank).Update(accountostadbank=course.price)
#         dpri.session.commit()
#     return flash("Inventory is not enough")

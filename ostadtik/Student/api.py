from flask import Blueprint, request, flash, jsonify

from ostadtik import db
from ostadtik.Student import Student
from flask_login import login_user, logout_user


__author__ = "NOROUZI"


student = Blueprint("Student", __name__)


@student.route("/register", methods=['POST', 'GET'])
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
        db.session.add(Student(username=username, passwordstudent=password, firstnamestudent=firstname,
                               lastnamestudent=lastname, email=email, staticphone=staticphone,
                               dynamicphone=dynamicphone, address=address, sex=sex, deposited=depositedy,
                               accountstudent=0, flag=False))

        db.session.commit()

    flash("User registered successfully !")
    return jsonify('hello')


@student.route('/login', methods=['GET'])
def login():
    username = request.json['']
    password = request.json['']

    stored_user = Student.query.filter_by(username=username).first()
    if stored_user is not None and stored_user.check_password(password):
        login_user(stored_user)
        flash("you are logged as {} to your account.")
        return jsonify('')
    else:
        flash("user or password is incorrect")
        return jsonify('')


@student.route('/logout')
def logout():
    logout_user()
    flash('you are logged out successfully !')
    return jsonify('')


@student.route('/update')
def update():
    updateaccont = request.json[""]

    Student.query.filter_by(Student.accountstudent).Update(accountstudent=updateaccont)
    db.session.commit()

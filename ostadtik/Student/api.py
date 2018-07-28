from flask import Blueprint, request, flash, jsonify

from ostadtik import db
from ostadtik.Student import Student
from flask_login import login_user, logout_user


__author__ = "NOROUZI"


student = Blueprint("Student", __name__)


@student.route("/register", methods=['POST', 'GET'])
def register():
    firstname = request.json['FirstName']
    username = request.json['UsreName']
    password = request.json['password']
    lastname = request.json['LastName']
    email = request.json['email']
    staticphone = request.json['StaticPhone']
    dynamicphone = request.json['DynamicPhone']
    address = request.json['Address']
    sex = request.json['Sex']
    accountstudent = request.json['AccountStudent']

    db.session.add(Student(username=username, passwordstudent=password, firstnamestudent=firstname,
                           lastnamestudent=lastname, email=email, staticphone=staticphone,
                           dynamicphone=dynamicphone, address=address, sex=sex,
                           accountstudent=accountstudent, flag=False))

    db.session.commit()


@student.route('/login', methods=['GET'])
def login():
    username = request.json['']
    password = request.json['']
    email = request.json['']

    stored_user = Student.query.filter_by(username=username, email=email).first()
    if stored_user is not None and stored_user.check_password(password):
        login_user(stored_user)
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

from flask import Blueprint, request, flash, jsonify

from ostadtik import db
from ostadtik.Student import Student
from flask_login import login_user


__author__ = "NOROUZI"


student = Blueprint("Student", __name__)


@student.route("/register", methods=['GET'])
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
    flag = request.json['Flag']

    db.session.add(Student(username=username, passwordstudent=password, firstnamestudent=firstname,
                           lastnamestudent=lastname, email=email, staticphone=staticphone,
                           dynamicphone=dynamicphone, address=address, sex=sex,
                           accountstudent=accountstudent, flag=flag))

    db.session.commit()


@student.route('/login', methods=['GET', "POST"])
def login():
    username = request.json['UsreName']
    password = request.json['password']
    email = request.json['Email']
    flag = Student.flag
    id = Student.Studentid

    stored_user = Student.query.filter_by(username=username, email=email).first()
    if stored_user is not None and stored_user.check_password(password):
        login_user(stored_user)
        return jsonify({"flag": flag, "studentid": id})
    else:
        return jsonify({"flag": 2})


@student.route('/update')
def update():
    updateaccont = request.json[""]

    Student.query.filter_by(Student.accountstudent).Update(accountstudent=updateaccont)
    db.session.commit()

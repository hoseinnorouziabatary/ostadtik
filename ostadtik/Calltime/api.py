from flask import Blueprint, request, jsonify, flash

from ostadtik.route import db
from ostadtik.Calltime import Call

__author__ = "NOROUZI"

calltime = Blueprint("calltime", __name__)


@calltime.route('/call', methods=['POST'])
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

    db.session.add(Call(azinhour=azinhour, tainhour=tainhour, azinminutes=azinminutes, tainminutes=tainminutes,
                        azinyy=azinyy, tainyy=tainyy, azinmm=azinmm, tainmm=tainmm, azindd=azindd, taindd=taindd))
    db.session.commit()

    flash("The operation was successful")
    return jsonify('')

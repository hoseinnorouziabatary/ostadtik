from flask import Blueprint, request

from ostadtik import db
from ostadtik.Calltime import Call

__author__ = "NOROUZI"

calltime = Blueprint("calltime", __name__)


@calltime.route('/call', methods=['POST'])
def cal():
    azinhour = request.json['StartHour']
    tainhour = request.json['EndHour']
    azinminutes = request.json['StartMinutes']
    tainminutes = request.json['EndMinutes']
    azinyy = request.json['StartYear']
    tainyy = request.json['EndYear']
    azinmm = request.json['StartMonth']
    tainmm = request.json['EndMonth']
    azindd = request.json['StartDay']
    taindd = request.json['EndDay']

    db.session.add(Call(azinhour=azinhour, tainhour=tainhour, azinminutes=azinminutes, tainminutes=tainminutes,
                        azinyy=azinyy, tainyy=tainyy, azinmm=azinmm, tainmm=tainmm, azindd=azindd, taindd=taindd))
    db.session.commit()

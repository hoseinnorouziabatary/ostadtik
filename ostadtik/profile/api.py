from flask import Blueprint, request

from ostadtik import db
from ostadtik.profile import Profile

__author__ = "NOROUZI"

profile = Blueprint("profile", __name__)


@profile.route('/register_profile', methods=["POST"])
def registerprofile():
    pdf = request.json['']
    video = request.json['']
    pictuer = request.json['']
    lastname = request.json['']
    firstname = request.json['']
    activenon = request.json['']

    db.session.add(Profile(pdf=pdf, video=video, pictuer=pictuer, lastname=lastname, firstname=firstname,
                           activenon=activenon))
    db.session.commit()

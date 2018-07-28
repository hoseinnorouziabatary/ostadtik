from flask import Blueprint, request

from ostadtik import db
from ostadtik.profile import Profile

__author__ = "NOROUZI"

profile = Blueprint("profile", __name__)


@profile.route('/register_profile', methods=["POST"])
def registerprofile():
    pdf = request.json['pdf']
    video = request.json['video']
    pictuer = request.json['pictuer']
    activenon = request.json['activenon']

    db.session.add(Profile(pdf=pdf, video=video, pictuer=pictuer,
                           activenon=activenon))
    db.session.commit()

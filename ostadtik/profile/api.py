from flask import Blueprint, request

from ostadtik import db
from ostadtik.profile import Profile

__author__ = "NOROUZI"

profile = Blueprint("profile", __name__)


@profile.route('/register_pdf', methods=["POST"])
def registerpdf():
    pdf = request.json['pdf']
    Profile.query.filter_by(Profile.pdf).Update(pdf=pdf)
    db.session.commit()


@profile.route('/register_video', methods=["POST"])
def registervideo():
    video = request.json['video']
    Profile.query.filter_by(Profile.video).Update(video=video)
    db.session.commit()


@profile.route('/register_pictuer', methods=['POST'])
def registerpictuer():
    pictuer = request.json['pictuer']
    Profile.query.filter_by(Profile.pictuer).Update(pictuer=pictuer)
    db.session.commit()


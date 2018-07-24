from flask import Flask


from ostadtik.Route.route import cal, clss, cmt, cour, prc, pro, stu, Tech

__author__ = "NOROUZI"

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://scott:root@localhost/OSTADTIK'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = b'\xaelX\x1fI\xa4\xfc{\xb8\x11Zk\xa1\xdb,\xf7L5[Bty\x1c\xb4'

app.register_blueprint(cal)
app.register_blueprint(clss)
app.register_blueprint(cmt)
app.register_blueprint(cour)
app.register_blueprint(prc)
app.register_blueprint(pro)
app.register_blueprint(stu)
app.register_blueprint(Tech)


if __name__ == "__main__":
    app.run(host="0.0.0.0", Debog=True, port=3000)


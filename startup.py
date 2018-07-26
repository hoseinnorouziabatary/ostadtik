from flask import Flask

from ostadtik import create_app

__author__ = "NOROUZI"

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:norouziabatary@localhost/OSTADTIK'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = b'\xaelX\x1fI\xa4\xfc{\xb8\x11Zk\xa1\xdb,\xf7L5[Bty\x1c\xb4'

app = create_app(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=3000)

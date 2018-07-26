

from flask_sqlalchemy import SQLAlchemy

__author__ = "NOROUZI"
dv = SQLAlchemy()


class Call(dv.Model):
    __table_name__ = "Call"
    calltimeid = dv.Column(dv.NVARCHAR(50), primary_key=True, unique=True, nullable=True)
    azinhour = dv.Column(dv.NVARCHAR(40), nullable=True)
    tainhour = dv.Column(dv.NVARCHAR(40), nullable=True)
    azinminutes = dv.Column(dv.NVARCHAR(40), nullable=True)
    tainminutes = dv.Column(dv.NVARCHAR(40), nullable=True)
    azinyy = dv.Column(dv.NVARCHAR(40), nullable=True)
    tainyy = dv.Column(dv.NVARCHAR(40), nullable=True)
    azinmm = dv.Column(dv.NVARCHAR(40), nullable=True)
    tainmm = dv.Column(dv.NVARCHAR(40), nullable=True)
    azindd = dv.Column(dv.NVARCHAR(40), nullable=True)
    taindd = dv.Column(dv.NVARCHAR(40), nullable=True)
    teacherid = dv.Column(dv.NVARCHAR(50), dv.ForeignKey('Teacher.TeacherID'), nullable=True)

    def __init__(self, azinhour, tainhour, azinminutes, tainminutes, azinyy, tainyy, azinmm, tainmm, azindd, taindd):
        self.azinhour = azinhour
        self.tainhour = tainhour
        self.azinminutes = azinminutes
        self.tainminutes = tainminutes
        self.azinyy = azinyy
        self.tainyy = tainyy
        self.azinmm = azinmm
        self.tainmm = tainmm
        self.azindd = azindd
        self.taindd = taindd

    def __repr__(self):
        return '<Calltime AzInHour{} TaInHour{} >' .format(self.azinhour, self.tainhour)

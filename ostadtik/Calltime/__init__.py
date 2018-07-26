from sqlalchemy import Column, NVARCHAR, ForeignKey

from ostadtik import db

__author__ = "NOROUZI"


class Call(db.Model):
    __table_name__ = "Call"
    calltimeid = Column(NVARCHAR(50), primary_key=True, unique=True, nullable=True)
    azinhour = Column(NVARCHAR(40), nullable=True)
    tainhour = Column(NVARCHAR(40), nullable=True)
    azinminutes = Column(NVARCHAR(40), nullable=True)
    tainminutes = Column(NVARCHAR(40), nullable=True)
    azinyy = Column(NVARCHAR(40), nullable=True)
    tainyy = Column(NVARCHAR(40), nullable=True)
    azinmm = Column(NVARCHAR(40), nullable=True)
    tainmm = Column(NVARCHAR(40), nullable=True)
    azindd = Column(NVARCHAR(40), nullable=True)
    taindd = Column(NVARCHAR(40), nullable=True)
    teacherid = Column(NVARCHAR(50), ForeignKey('Teacher.TeacherID'), nullable=True)

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

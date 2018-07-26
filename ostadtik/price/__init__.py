
from flask_sqlalchemy import SQLAlchemy


__author__ = "NOROUZI"

dpri = SQLAlchemy()


class Pricetable(dpri.Model):
    __table_name__ = "price"
    pricetableid = dpri.Column(dpri.NVARCHAR(50), primary_key=True, unique=True, nullable=True)
    accountostadbank = dpri.Column(dpri.NVARCHAR(40), nullable=False)
    classtableid = dpri.Column(dpri.NVARCHAR(50), dpri.ForeignKey('Class.ClassTableID'), nullable=True)
    accountstudent = dpri.Column(dpri.NVARCHAR(40), dpri.ForeignKey('student.Account'), nullable=False)
    price = dpri.Column(dpri.INT, dpri.ForeignKey('ClassTable.price'), nullable=True)
    lastnamestudent = dpri.Column(dpri.NVARCHAR(40), dpri.ForeignKey('ClassTable.LastNameStudent'), nullable=True)
    lastnameteacher = dpri.Column(dpri.NVARCHAR(40), dpri.ForeignKey('ClassTable.LastNameTeacher'), nullable=True)

    def __init__(self, accountostadbank):
        self.accountostadbank = accountostadbank

    def __repr__(self):
        return '< PriceTable Table{}'.format(self.__tablename__)

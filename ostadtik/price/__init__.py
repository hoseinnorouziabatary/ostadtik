from sqlalchemy import Column, NVARCHAR, ForeignKey, INTEGER

from ostadtik import db

__author__ = "NOROUZI"


class Pricetable(db.Model):
    __table_name__ = "price"
    pricetableid = Column(NVARCHAR(50), primary_key=True, unique=True, nullable=True)
    accountostadbank = Column(NVARCHAR(40), nullable=True, unique=True)
    classtableid = Column(NVARCHAR(50), ForeignKey('Class.ClassTableID'), nullable=True)
    accountstudent = Column(NVARCHAR(40), ForeignKey('student.Account'), nullable=False)
    price = Column(INTEGER, ForeignKey('ClassTable.price'), nullable=True)
    lastnamestudent = Column(NVARCHAR(40), ForeignKey('ClassTable.LastNameStudent'), nullable=True)
    lastnameteacher = Column(NVARCHAR(40), ForeignKey('ClassTable.LastNameTeacher'), nullable=True)

    def __init__(self, ostadbank):
        self.accountostadbank = ostadbank

    def __repr__(self):
        return '< PriceTable Table{}'.format(self.__tablename__)

# A CLASS IS A BLUEPRINT or a prototypr that is a collectio of related properties and methods

class Student:
    # Class variables-variales that are shared across all instances
    reg_no=""
    grade=""
    totalmarks=""
    avaragemarks=""
    def __init__(self,math,eng,swa,science,sst):
    def totalMarks(self,math,eng,swa,science,sst):
        self.totalmarks=math+eng+swa+science+sst




    def calculateaverage(self,tot):
        self.avaragemarks=tot/5

# variable brian is an object of a class?
# An objectis an instance ofa class

brian =Student()
# # funbctionsinsidea class is a method

class Student :          
    def __init__(self,name,roll_no,age,marks):
        self.__name = name
        self.__roll_no = roll_no
        self.__age = age 
        self.__marks = marks
        self.__result = self.calculate_result(marks)
    def get_marks(self) :
        return self.__marks
    def set_marks (self,marks):
        self.__marks = marks 
        self.__result = self.calculate_result(marks)
    def get_name(self) :
        return self.__name
    def set_name(self,name) :
        self.__name = name
    def get_age(self) :
        return self.__age
    def set_age(self,age) :
        self.__age = age
    def get_roll_no(self) :
        return self.__roll_no
    def get_result(self) :
        return self.__result
    def calculate_result(self,marks):
        if marks >= 90:
            return "Excellent"
        elif marks >= 80:
            return "Good"
        elif marks >= 50:
            return "Only Pass"
        else:
            return "Fail"
"""
Method:The function inside a class is called  as method.
There are three types of methods as
1) instance method
2) class methods
3) static methods


1) instance method:
-work on the instance variable
-first argument is 'self'
-it also able to work on class and local vriable
-it can call using object ReferenceError
"""

# class Student:
#     # class/static variable
#     course="python"
#     trainer="vaibhav"
#     institute="jbk"
#     def __init__(self,nm,ag,ct,per):
#         self.name=nm
#         self.age=ag
#         self.city=ct
#         self.percentage=per
#     def details(self):
#         return f"""
#             Name={self.name}
#             Age={self.age}
#             City={self.city}
#             Percentage={self.percentage}
#             Course={Student.course}
#             Course={self.course}
#         """
# s1=Student("jay",21,"pune",89)
# s2=Student("ajay",23,"nagpur",78)
# print(s1.details())
# print(s2.details())

#_______________________________________________________________________________________

"""
2) class method:
- It can work only on static/class variable.
-first paramether is 'cls'
-use the decorator '@classmethod' is mandatory
-call using classname or object reference.
"""


# class Student:
#     # class/static variable
#     course="python"
#     trainer="vaibhav"
#     institute="jbk"
#     def __init__(self,nm,ag,ct,per):
#         # instance variable
#         self.name=nm
#         self.age=ag
#         self.city=ct
#         self.percentage=per
#     # instance method
#     def details(self):
#         return f"""
#             # Name={self.name}
#             # Age={self.age}
#             # City={self.city}
#             # Percentage={self.percentage}
#             # Course={Student.course}
#             # Course={self.course}
#           """
#     # class method
#     @classmethod
#     def class_details(cls):
#      return f"""
#         Course={cls.course}
#         Trainer={cls.trainer}
#         Institute={cls.institute}
#       """
# s1=Student("jay",21,"pune",89)
# s2=Student("ajay",23,"nagpur",78)
# print(s1.details())
# print(s2.details())
# print(Student.class_details())
# print(s1.class_details())

#__________________________________________________________________________________________

"""
#3) static method:
- It can work on the local variables.
-There is no first parameter for reference.
-use the decorator '@staticmethod'
-call using object reference.
"""


# class Student:
#     # class/static variable
#     course="python"
#     trainer="vaibhav"
#     institute="jbk"
#     def __init__(self,nm,ag,ct,per):
#         # instance variable
#         self.name=nm
#         self.age=ag
#         self.city=ct
#         self.percentage=per
#     # instance method
#     def details(self):
#         return f"""
#             Name={self.name}
#             Age={self.age}
#             City={self.city}
            # Percentage={self.percentage}
            # Course={Student.course}
            # Course={self.course}
            # """
#     # class method
#     @classmethod
#     def class_details(cls):
#      return f"""
#         Course={cls.course}
#         Trainer={cls.trainer}
#         Institute={cls.institute}
# """
#     # static method
#     @staticmethod
#     def cal_per(m1,m2,m3):
#        perc=(m1+m2+m3)/3
#        return perc
# s1=Student("jay",21,"pune",89)
# s2=Student("ajay",23,"nagpur",78)
# print(s1.cal_per(74,67,56))

#_______________________________________________________________________________________________________

# class Employee:
#       company="wipro"
#       location="Chennai"
#       def __init__(self,nm,ct,mn,sal):
#             self.name=nm
#             self.city=ct
#             self.mono=mn
#             self.salary=sal
#       def emp_details(self):
#             return f"""
#             Name={self.name}
#             City={self.city}
#             Mono={self.mono}
#             Salary={self.salary}
#             Location={self.location}
#         """
#       #class method
#       @classmethod
#       def class_details(cls):
#             return f"""
#                Company={cls.company}
#                Location={cls.location}
#         """
#       def TDS(self):
#             package=self.salary*12
#             if package<300000:
#                   return "no TDS"
#             elif package<600000:
#                   package=package*5/100
#                   return package
#             elif package<100000:
#                   package=package*10/100
#                   return package
#             elif package>100000:
#                   package=package*20/100
#                   return package
# e1=Employee("Mahesh","Pune",56634743,34000)
# e2=Employee("Ram","Nagpur",564589389,23000)
# print(e1.emp_details())
# print(Employee.class_details()) 
# print(e1.TDS())     


class Mobile:
    brand="oneplus"
    company="apple"
    def __init__(self,model,ram,camera,color,price):
        self.model=model
        self.ram=ram
        self.camera=camera
        self.color=color
        self.price=price
    #instance method
    def display_details(self):
        return f"""
            Model of mobile={self.model}
            Ram of mobile={self.ram}
            Camera of mobile={self.camera}
            Color of mobile={self.color}
            Price of mobile={self.price}
            Brand of mobile={self.brand}
      """
    #class method
    @classmethod
    def class_details(cls):
        return f"""
            Brand of mobile={cls.brand}
            Company of mobile={cls.company}
      """
    # def GST(self,per):
    #     GST_amt=self.price*per/100
    #     return GST_amt
    # def cal_disc(self):
    #     disc_amt=self.price*10/100
    #     return disc_amt
    @staticmethod
    def incr_GST(GST_rate,per):
        GST_rate=GST_rate+per
        return GST_rate
    #instance method
    def selling_price(self,GST_rate,disc_rate):
        selling_price=self.price+(self.price*GST_rate/100)-(self.price*disc_rate/100)
        return selling_price
m1=Mobile("O15","16GB","125px","white",23000)
m2=Mobile("O19","28GB","128px","silver",30000)
print(m1.selling_price(10,5))
print(m2.class_details())
print(m2.selling_price(34,20))
print(m2.incr_GST(10,3))
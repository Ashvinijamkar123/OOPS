## class,constructor,object:

# class Student:
#     def __init__(self):                                 # constructor is a special method called __init__ which can be
#         print(f"id of self is {id(self)}")               # defined using def keyword.functions inside the class called as methods.
#     def details():                                        # self is first paramete of method which takes id of reference variable.
#         print("hello")
# s1=Student()
# print(f"id of s1 is {id(s1)}")                      # self is an object reference,it is execute for each object
# print("-"*100)
# s2=Student()
# print(f"id of s2 is {id(s2)}")


# class Student():
#     def __init__(self,name,city,per):                                 # constructor is a special method called __init__ which can be de
#         self.name=name
#         self.city=city
#         self.percentage=per
#     def details():
#         print("hello")
# s1=Student("jay","Nashik",67)
# s2=Student("Mahesh","Pune",89)


## instance variable
# class Student:
#     course="python"
#     trainer="Vaibhav Patil"                     # class/static variable
#     def __init__(self,nm,ct,ag,per):
#         self.name=nm
#         self.city=ct                            # instance variable
#         self.age=ag
#         self.percentage=per
# s1=Student("mahesh","nashik",23,56)
# s2=Student("ajay","pune",24,68)
# print(s1.name)
# s1.name="rahul"
# print(s1.name)
# print(s2.name)
# print(Student.course)


# class Employee:
#     company="Wipro"
#     def __init__(self,nm,ct,mn,dept,sal):
#         self.name=nm
#         self.city=ct
#         self.mobile=mn
#         self.department=dept
#         self.salary=sal
# e1=Employee("Mahesh","Nashik",45737998,"HR",34000)
# e2=Employee("Prathmesh","Nagpur",42367828,"testing",45000)
# print(e2.department)
# print(Employee.company)
# e1.salary=40000
# print(e1.salary)


# class Mobile:
#     company="samsung"
#     def __init__(self,model,sto,ram,price):
#         self.Model=model
#         self.storage=sto
#         self.Ram=ram
#         self.Price=price
# m1=Mobile("s23","28GB","8GB",21000)
# m2=Mobile("s44","52GB","12GB",34000)
# print(m1.Ram)

#_______________________________________________________________________________________________


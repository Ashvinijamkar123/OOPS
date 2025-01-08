
""""
-Abstract class is class in which there is abstact and noabstact methods.ModuleNotFoundError
-To crete abstract class,we need to inherit the ABC class into our class from abc module.
-It is mandatory to keep at least on abstract method in abstract class.abstractmethod
-object of abstract class in not created.credits
-To create abstarct method,usded @abstractmethod decorator.
=It is mandatory to implement all the methods within abstract class in the our class.
-If there are all the methods in abstract class are abstract,it is called interface.
-If any method in abstract class is nonabstract,it is called abstract class.
"""

# from abc import ABC,abstractmethod
# class XYZ(ABC):
#     @abstractmethod
#     def display():
#         pass
# x=XYZ()


# from abc import ABC,abstractmethod
# class RBI(ABC):
#     @abstractmethod
#     def ifsc(self):
#         pass
#     @abstractmethod
#     def branchname(self):
#         pass
#     @abstractmethod
#     def crop_loan(self):
#         pass
# class Sbi(RBI):
#     def ifsc(self):
#         return f"IFSC code of Sbi=SBI56478829"
#     def branchname(self):
#         return f"Branch name is karvenagar"
#     def crop_loan(self):
#         return f"crop loan rate is 8%"
# s=Sbi()
# print(s.branchname())
# class Cbi(RBI):
#     def ifsc(self):
#         return f"IFSC code of Sbi=CBI56434829"
#     def branchname(self):
#         return f"Branch name is Warje"
#     def crop_loan(self):
#         return f"crop loan rate is 10%"
# c=Cbi()
# print(c.ifsc())
# class Bom(RBI):
#     def ifsc(self):
#         return f"IFSC code of Sbi=BOM64737827"
#     def branchname(self):
#         return f"Branch name is Kothrud"
#     def crop_loan(self):
#         return f"crop loan rate is 7%"
# b=Bom()
# print(b.crop_loan())


# from abc import ABC,abstractmethod
# class ATM(ABC):
#     @abstractmethod
#     def bank_name(self):
#         pass
#     @abstractmethod
#     def pin(self):
    #     pass
    # @abstractmethod
    # def withdraw(self):
        # pass
# class SBI(ATM):
#     def bank_name(self):
#         return "bank name is State bank of India"
#     def pin(self):
#         return "customer pin is 4567"
#     def withdraw(self):
#         return "withdraw amount is 1000"
# class BOB(ATM):
#     def bank_name(self):
#         return "bank name is State bank of baroda"
#     def pin(self):
#         return "customer pin is 6754"
#     def withdraw(self):
#         return "withdraw amount is 50000"
    

from abc import ABC,abstractmethod
class Car(ABC):
    @abstractmethod
    def company(self):
        pass
    @abstractmethod
    def average(self):
        pass
    @abstractmethod
    def color(self):
        pass
    @abstractmethod
    def insurance(self):
        pass
class Toyota(Car):
    def company(self):
        return f"Company of car is TATA"
    def average(self):
        return "average of car is 100 km/hr"
    def color(self):
        return "color of car is brown."
    def insurance(self):
        return "insurance of car is 30%"
t=Toyota()
print(t.insurance())
class Swift(Car):
    def company(self):
        return f"Company of car is Suzuki"
    def average(self):
        return "average of car is 90 km/hr"
    def color(self):
        return "color of car is white."
    def insurance(self):
        return "insurance of car is 34%"
s=Swift()
print(s.color())
class Thar(Car):
    def company(self):
        return f"Company of car is Honda"
    def average(self):
        return "average of car is 120 km/hr"
    def color(self):
        return "color of car is black."
    def insurance(self):
        return "insurance of car is 45%"
t1=Thar()
print(t1.average())




    


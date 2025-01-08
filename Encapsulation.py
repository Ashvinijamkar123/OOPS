##Public variable
# class Counter:
#     def __init__(self):
#         self.count=0                # public variable
#     def inc(self):
#         self.count=self.count+1
#     def dec(self):
#         self.count=self.count-1
#     def check(self):
#         return self.count
# c=Counter()
# print(c.check())
# c.inc()                             # public variable can be access outside of class using object reference 
# c.inc()                             # and they also modify outside of class
# c.inc()
# print(c.check())
# c.dec()
# print(c.check())
# c.count=999
# print(c.check())
     

## Private variable:
# class Counter:
#     def __init__(self):
#         self.__count=0                # private variable
#     def inc(self):
#         self.__count=self.__count+1
#     def dec(self):
#         self.__count=self.__count-1
#     def check(self):
#         return self.__count
# c=Counter()
# print(c.check())
# c.inc()                             # private variable can not be access outside of class using object reference 
# c.inc()                             # and they are not  modify outside of class
# c.inc()
# print(c.check())
# c.dec()
# print(c.check())
# print(c.count)
# # print(c.__count)
# c.count=999
# c.name="gayu"
# print(c.name)

#______________________________________________________________________________________________________

# class Finance:
#     def __init__(self):
#         self.revenue=10000
#     def check_revenue(self):
#         return self.revenue
# f=Finance()

# class Hr:
#     def __init__(self):
#         self.no_emp=100
#     def change(self):
#         f.revenue=0
#     def check(self):
#         return f.revenue
# h=Hr()
# print(f.check_revenue())
# print(h.check())



class Finance:
    def __init__(self):
        self.__revenue=10000
    def check_revenue(self):
        return self.__revenue
f=Finance()

class Hr:
    def __init__(self):
        self.no_emp=100
    def change(self):
        f.__revenue=0
    def check(self):
        return f.__revenue
h=Hr()
#print(h.check())
print(f.check_revenue())
print(h.check())



        
     

# class Book:
#     def __init__(self,bname,pg):
#         self.name=bname
#         self.pages=pg
# b1=Book("xyz",300)
# b2=Book("abc",200)
#print(b1.pages+b2.pages)
# print(300+200)
# print(b1+b2)              #There is no __add__ method for class object hence addition is not possible


# class Book:
#     def __init__(self,bname,pg):
#         self.name=bname
#         self.pages=pg
#     def __add__(self,other):                    # we can create the __add__ method within class and call it
#         return self.pages+other.pages
# b1=Book("xyz",300)
# b2=Book("abc",200)
# b3=Book("pqr",100)
# print(b1+b2)



# class Book:
#     def __init__(self,bname,pg):
#         self.name=bname
#         self.pages=pg
#     def __add__(self,other):                    # we can create the __add__ method within class and call it
#         return self.pages+other.pages
# b1=Book("xyz",300)
# b2=Book("abc",200)
# b3=Book("pqr",400)
# print(b1+b2+b3)


class Book:
    def __init__(self,bname,pg):
        self.name=bname
        self.pages=pg
    def __add__(self,other):                    # we can create the __add__ method within class and call it
        total=self.pages+other.pages
        return Book("x",total)
    # def __str__(self):
    #     return str(self.pages)
b1=Book("xyz",300)
b2=Book("abc",200)
b3=Book("pqr",400)
print(b1+b2+b3)



#_____________________________________________________________________________________________________

# class Hotel:
#     def __init__(self,name,rent):
#         self.name=name
#         self.rent=rent
# h1=Hotel("raj",10000)
# h2=Hotel("taj",5000)
# print(h1.rent>h2.rent)
# print(10000>5000)
# print(h1>h2)

# class Hotel:
#     def __init__(self,name,rent):
#         self.name=name
#         self.rent=rent
#     def __gt__(self,other):
#         return self.rent>other.rent
# h1=Hotel("raj",10000)
# h2=Hotel("taj",5000)
# print(h1>h2)




#________________________________________________________________________________________
## Method overloading:There is no method overloading in python.If we try to method overloading,the latest method is executed.

# class Calci:
#     def add(self,n1,n2):
#         return n1+n2
#     def add(self,n1,n2,n3):
#         return n1+n2+n3
#     def add(self,n1,n2,n3,n4):
#         return n1+n2+n3+n4
# c=Calci()
# print(c.add(10,20,23,7))
        
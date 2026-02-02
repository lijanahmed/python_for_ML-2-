#classmethod.

class person:
    name= "no Name"
    def __init__(self,nm):
        self.name=nm

p1=person("sakib")
print(p1.name)
print(person.name)

# if i want to change the name of class.
print("===================")
#no.1
class person:
    name= "no Name"
    def __init__(self,nm):
        person.name=nm #direct acces in class

p1=person("sakib")
print(p1.name)
print(person.name)
print("===================")

#no2.
class person:
    name= "no Name"
    def __init__(self,nm):
        self.__class__.name=nm #this= (object's class)

p1=person("sakib")
print(p1.name)
print(person.name)
print("===================")

#no 3. (Using the decorator )
class person:
    name= "No Name"
    @classmethod
    def Change_name(cls,nm): # as self= obj, So cls= Class
        cls.name=nm
        return cls.name

p1=person()
print(p1.Change_name("Sakib"))
print(person.name)

# here i learn 3 type of method , 
# 1. normal method/ intrans method (slef = object)
#   self.anythig means  obj access
# 2. classmethod (cls = class)
#   cls.anything = class access
# 3. staticmethod ( no parameter)


print("======polymorphism=======")

class complex:
    def __init__(self,real, img):
        self.real = real
        self.img= img
    def showNumber(self):
        print(f"{self.real} + {self.img}i")

    def add (self,newNum):
        self.newReal= self.real + newNum.real
        self.newImg = self.img + newNum.img
        return complex(self.newReal,self.newImg)


num1= complex(2,5)
num1.showNumber()
num2= complex(4,10)
num2.showNumber()
num3= num1.add(num2)
num3.showNumber()

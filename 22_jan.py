class Lijan:
    identity= "visitor"
    # identity is same for everyone , so no need to make extra memory storage.
    def __init__(self,name):
        self.nm= name
        print(f"wecome {self.nm}, to my world.")

    def wecome(self):
        print("welcome you are here")

    def showName(self):
        return self.nm

l1= Lijan("avik")
print(l1.nm)
print(l1.nm , "is a ", Lijan.identity)

l2= Lijan("badsha")
print(l2.nm)
print(l2.nm , "is a ", Lijan.identity)

l1.wecome()
print(l1.showName())
l2.wecome()
print(l2.showName())


# public privet 
class BackAccount:
    def __init__(self, accNo,accPass):
        print ("you are welcome")
        
        self.accNo= accNo
        self.__accPass= accPass  # this is a privet attribute
    
    def resetPass(self,new_pass):
        print(self.__accPass)
        self.__accPass= new_pass
        print(self.__accPass)

bk= BackAccount(12345,"a1234")
print(bk.resetPass("112233"))
# print(bk.__accPass)



# inharitance 
class A:
    varA= " this is class A"
class B(A):
    varB= " this is class B"
class C(B): # Multi Lebel inheritage
    varC= " this is class C"

objC=C
print(objC.varA)
print(objC.varB)
print(objC.varC)


class A:
    varA= " this is class A"
class B:
    varB= " this is class B"
class C(A,B): # multi inheritance
    varC= " this is class C"

print(objC.varA)
print(objC.varB)
print(objC.varC)




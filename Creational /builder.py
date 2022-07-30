class User:
    def __init__(self,name):
        self.name = name

class UserBuilder:
    def __init__(self,name):
        self.user= User(name)
        
    def setAge(self,age):
        self.user.age=age
           
    def setPhone(self,phone):
        self.user.phone=phone
 
    def setAddress(self,address):
        self.user.address=address
   
    def build(self):
        return self.user

user = UserBuilder('Ram')
user.setAge(15)
user.setPhone(9654123658)
user.setAddress('Mumbai')
print(user.build().name)
print(user.build().age)
print(user.build().phone)
print(user.build().address)


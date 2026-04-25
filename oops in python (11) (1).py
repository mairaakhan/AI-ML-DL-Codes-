class Myclass:
    x = 5
p1 = Myclass()
p2 = Myclass()
p3 = Myclass()

print(p1.x)

#will del p1 
# del p1
# print(p1.x)

print(p2.x)
print(p3.x)

#class can not be empty so we use pass 
class Person:
    pass

#With __init__ → Object is ready when created ,#It does not return anything.
#Without __init__ → Object is empty, you must fill it manually
#'self' does not has to be name self 
    
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = person('Maira',22)

print('Name:' ,p1.name)
print('Age:' ,p1.age)

class person:
    def __init__(a, name, age):
        a.name = name
        a.age = age

p1 = person('Maira',22)
p2 = person('Khan',21)

print('Name:' ,p1.name)
print('Age:' ,p1.age)

print('Name:' ,p2.name)
print('Age:' ,p2.age)

#without __init__ u need to set properties manually
class Person:
    pass

p1 = Person()
p1.name = "Maira"
p1.age = 22

print(p1.name)
print(p1.age)


#with default values
class person:
    def __init__(self, name, age = 18):
        self.name = name
        self.age = age
        
p1 = person('Maira',22)
print('Name:' ,p1.name)
print('Age:' ,p1.age)

print()

p2 = person('Maira')
print('Name:' ,p2.name)
print('Age:' ,p2.age)

class person:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country
        
p1 = person('Maira', 22, 'karachi', 'pakistan')

print('Name:' ,p1.name)
print('Age:' ,p1.age)
print('city:' ,p1.city)
print('country:' ,p1.country)

#Exercise

class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    def bark(self):
        print(self.name + ' says woof!')
d1 = dog('buddy', 6)
d1.bark()

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print('hello my name is: ' + self.name)

p1 = person('Maira',22)
p1.greet()

#properties
class person:
    def __init__(self, name):
        self.name = name

    def printname(self):
        print(self.name)

p1 = person('Maira')
p2 = person('john')

p1.printname()
p2.printname()

#here we change the self name as k
class person:
    def __init__(k, name, age):
        k.name = name
        k.age = age

    def greet(k):
        print('hello my name is: ' + k.name)

p1 = person('Maira',22)
p1.greet()

class car:
    def __init__(self, model, brand, year):
        self.model = model
        self.brand = brand 
        self.year = year
    def display_info(self):
        print(f'{self.model} {self.brand} {self.year}')

car1 = car('toyota', 'corolla', 2016)
car1.display_info()

class person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return 'hello,' + self.name

    def welcome(self):
        message = self.greet()
        print(message + '! welcome here')

p1 = person('Maira')
p1.welcome()




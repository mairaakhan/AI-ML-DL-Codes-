#inheritance

class Parent:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

x = Parent("Maira", "Khan")
x.printname()

class Child(Person):
  pass

x = Child("Maira", "Khan")
x.printname()


#Child class with init 

class Parent:
    def __init__(self, FirstName, LastName):
        self.FirstName = FirstName
        self.LastName =  LastName

class child(Parent):
    def __init__(self, FirstName, LastName, age):
        Parent.__init__(self, FirstName, LastName)
        self.age = age
        
    def called(self):
        print(self.FirstName ,self.LastName, self.age)
        
c = child('Maira', 'Khan', 22)
c.called()

#Child class with init using super()

class Parent:
    def __init__(self, FirstName, LastName):
        self.FirstName = FirstName
        self.LastName =  LastName

class child(Parent):
    def __init__(self, FirstName, LastName, age):
        super().__init__(FirstName, LastName)
        self.age = age
        
    def called(self):
        print(self.FirstName ,self.LastName, self.age)
        
c = child('Maira', 'Khan', 22)
c.called()

#The word “polymorphism” means many forms.
#In programming, it means the same function/method can work on different objects or classes. example len()

#len() with a string
x = "Maira Khan"
print(len(x))

#len() with tuple
x = ("Maira", "Khan")
print(len(x))

#len() with dictionary
x = {"First Name:" : "Maira",  "Last Name:" : "Khan"}
print(len(x))

class car:
    def __init__(self,brand):
        self.brand = brand
    def move(self):
        print(self.brand , "is moving")

class aeroplane:
    def __init__(self,brand):
        self.brand = brand
    def move(self):
        print(self.brand , "is flying")

class boat:
    def __init__(self,brand):
        self.brand = brand
    def move(self):
        print(self.brand , "is sailing")

class man:
    def __init__(self,name):
        self.name = name
    def move(self):
        print(self.name , "is running")

c = car("BMW")
a = aeroplane("Emirates")
b = boat("xyz")
m = man("john")

#without for loop
# c.move()
# a.move()
# b.move()
# m.move()

#with for loop
for i in (c,a,b,m):
    i.move()

# Inheritance Class Polymorphism
class Parent:
    def __init__(self,brand):
        self.brand = brand
    def move(self):
        print(self.brand , "is moving")

class aeroplane(Parent):
    def move(self):
        print(self.brand , "is flying")

class boat(Parent):
    def move(self):
        print(self.brand , "is sailing")

c = Parent("BMW")
a = aeroplane("Emirates")
b = boat("xyz")

#without for loop
# c.move()
# a.move()
# b.move()
# m.move()

#with for loop
for i in (c,a,b):
    i.move()

#Encapsulation = Keeping data (properties) and methods together inside a class.
#Controls how data is accessed/modified from outside the class.
#Protects data from accidental changes.
#Use double underscore __ to make a property private.

class person:
    def __init__(self, name, age):
        self.name = name
        self.__age =  age
p = person('Maira',22)
print(p.name)
# print(p.age) it will give error cause its private

#getter & setter

class person:
    def __init__(self, name, age):
        self.name = name
        self.__age =  age
    def get_age(self):
        return self.__age
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print('must be greater than 0')
p = person('Maira',22)
print(p.name)
print(p.get_age())
p.set_age(21)
print(p.get_age())

#Example with Validation
class person:
    def __init__(self, name):
        self.name = name
        self.__age =  0
    
    def set_age(self, age):
        if 0 <= age <= 100:
            self.__age = age
        else:
            print('must be greater than 0 and less than 100')

    def get_age(self):
        return self.__age
        
p = person('Maira')
print(p.name)
p.set_age(21)
print(p.get_age())

p.set_age(-1)

class Person:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary  # protected

p1 = Person("Linus", 50000)
print(p1._salary)  # works, but “internal use”

# Example
# Create a private method:
#__validate has double underscores (__) → it is a private method.
#Private methods cannot be accessed directly from outside the class.
#You can only call them from inside the class, like in add().

class Calculator:
  def __init__(self):
    self.result = 0

  def __validate(self, num):
    if not isinstance(num, (int, float)):
      return False
    return True

  def add(self, num):
    if self.__validate(num):
      self.result += num
    else:
      print("Invalid number")

calc = Calculator()
calc.add(10)
calc.add(5)
print(calc.result)
# calc.__validate(5) # This would cause an error

# Python Name Mangling Example

class Person:
    def __init__(self, name, age):
        self.name = name      # public property
        self.__age = age      # private property (double underscore)

p1 = Person("Maira", 22)
print(p1.name)

# Try to access private property directly (will cause error)
# print(p1.__age)  # Uncommenting this line will raise AttributeError

# Access private property using name mangling (not recommended)
print("Age via name mangling:", p1._Person__age)

# Access the inner class and create an object:
class Outer:
    def __init__(self):
        self.name = "Outer Class"

    class Inner:
        def __init__(self):
            self.name = "Inner Class"

        def display(self):
            print("This is the inner class")

outer = Outer()
print(outer.name)        # Outer Class

inner = outer.Inner()    # Create inner class object
inner.display()          # This is the inner class

# Accessing Outer Class from Inner Class
# Inner classes in Python do not automatically have access to the outer class instance.
# If you want the inner class to access the outer class, you need to pass the outer class instance as a parameter:

class Outer:
    def __init__(self):
        self.name = "Emil"

    class Inner:
        def __init__(self, outer):
            self.outer = outer

        def display(self):
            print(f"Outer class name: {self.outer.name}")

outer = Outer()
inner = outer.Inner(outer)
inner.display()   # Outer class name: Emil

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.engine = self.Engine()   # Inner class instance

    class Engine:
        def __init__(self):
            self.status = "Off"

        def start(self):
            self.status = "Running"
            print("Engine started")

        def stop(self):
            self.status = "Off"
            print("Engine stopped")

    def drive(self):
        if self.engine.status == "Running":
            print(f"Driving the {self.brand} {self.model}")
        else:
            print("Start the engine first!")

car = Car("Toyota", "Corolla")
car.drive()        # Start the engine first!
car.engine.start() # Engine started
car.drive()        # Driving the Toyota Corolla

#Multiple Inner Classes

class Computer:
    def __init__(self):
        self.cpu = self.CPU()
        self.ram = self.RAM()

    class CPU:
        def process(self):
            print("Processing data")

    class RAM:
        def store(self):
            print("Storing data")

computer = Computer()
computer.cpu.process()   # Processing data...
computer.ram.store()     # Storing data...




#class task
class Car:
    def __init__(self,brand):
        self.brand = brand
    def show(self):
        print(self.brand)
c1 = Car("Ford")
c1.show()

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = person("maira",22)
print(p1.name , p1.age)

p1.age = 21
print(p1.age)

#deleting
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = person('maira',22)
p2 = person('khan',23)

del p2.name

print(p1.name , p1.age)

# print(p2.name) #it will through an error b/c its deleted
print(p2.age)


class person:
    species = "human"
    
    def __init__(self,name):
        self.name = name #instance property

p1 = person('maira')
print(p1.name)
print('p1 species:',p1.species)

print()

p2 = person("john")
print(p2.name)
print('p2 species:',p2.species)

    

class person:
    lastname = ""
    
    def __init__(self,name):
        self.name = name 

p1 = person('maira')
p2 = person("john")
person.lastname = "khan"

print(p1.name , p1.lastname)
print(p2.name , p2.lastname)


#This class only defines one attribute by default: name.
class person: 
    def __init__(self,name):
        self.name = name 

p1 = person('maira')
p2 = person("john")

# Dynamically add a new attribute 'age' to object p1
p1.age = 22
# Dynamically add a new attribute 'city' to object p1
p1.city = "karachi"

print(p1.name)
print(p2.name)
print(p1.age)
print(p1.city)

# This will give an error because p2 does not have 'age' and 'city' attributes
# print(p2.age)
# print(p2.city)

class cal:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

calculator = cal()

print(calculator.add(1, 2))
print(calculator.multiply(2, 3))

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1
        print(f'happy birthday {self.name} you are now {self.age} years old')

p1 = person('Maira', 22)
p1.birthday()
p1.birthday()

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return(f"{self.name} ({self.age})")

    def __repr__(self):
        return(f"{self.name} ({self.age})")
        
    def birthday(self):
        self.age += 1
        print(f'happy birthday {self.name} you are now {self.age} years old')

p1 = person('Maira', 22)
print(p1)
print(p1.birthday())
print(repr(p1))

class playlist:
    def __init__(self,name):
        self.name = name
        self.songs = []

    def add_song(self,song):
        self.songs.append(song)
        print(f'Song Added: {song}')
    
    def del_song(self,song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"song removed: {song}")

    def show_song(self):
        print(f'playlist: {self.name}')
        for song in self.songs:
            print(f'{song}')

my_playlist = playlist("fav")
my_playlist.add_song("xyz")
my_playlist.add_song("abc")
my_playlist.show_song()
# my_playlist.remove.song()
# my_playlist.del.song()

    




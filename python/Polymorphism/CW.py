class Nepali:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Namaste, Mero naam {self.name} ho!"


class English:
    def __init__(self, name):
        self.name = name
    def greet(self):
        return f"Hello I am {self.name}."


hari = Nepali("Hari")
harry = English("Harry")
print(hari.greet())
print(harry.greet())

class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()
    
#Method overriding:= if same method/function is defined on child and parent then child logic is implemented
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

d = Dog()
d.sound()
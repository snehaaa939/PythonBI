class Car:
    def __init__(self, color, model, year=2026):  # constructor
        self.brand = "ABC Inc"
        self.color = color
        self.model = model
        self.year = year

    # methods
    def start_car(self):
        print(f"{self.model} car is starting")

    def stop_car(self, rate):
        print(f"{self.model} car is stopping at rate {rate}")


car_1 = Car("red", "Toyota")
car_2 = Car("blue", "Ford", 2025)
car_1.start_car()
car_1.stop_car(-2)

print(car_1.brand, car_1.color, car_1.model)
print(car_2.brand, car_2.color, car_2.model, car_2.year)

# Create a class named as player with necessary attributes.
# Create 3 objects from this class , One forward, One defender and one Mid-Fielder


class Player:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position


player1 = Player("Messi", 36, "Forward")
player2 = Player("Ramos", 38, "Defender")
player3 = Player("Modric", 39, "Mid-Fielder")

print(player1.name, player1.age, player1.position)
print(player2.name, player2.age, player2.position)
print(player3.name, player3.age, player3.position)

# add methods shoot(that has argument speed).
# Call this function with first_object.
# While call this function output has to : {player_name} is shooting as {speed}


class Player:
    def __init__(self, player_name):
        self.player_name = player_name

    def shoot(self, speed):
        print(f"{self.player_name} is shooting at {speed}")


first_object = Player("Messi")
first_object.shoot(85)


# INHERITANCE

class People:
    def __init__(self, name, height, skin_color, behavior, age):
        self.name = name
        self.height = height
        self.skin_color = skin_color
        self.behavior = behavior
        self.age = age


# Create a class mammal with relevant attribute and at least one method walk
# Create another class Elephant inheriting mammal. Add other necessary argument and one more extra method named ride
# Create an object named Ronaldo from Elephant class
# Call methods .walk() and .ride() on this object


class Mammal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f"{self.name} is walking.")


class Elephants(Mammal):
    def __init__(self, name):
        super().__init__(name)

    def ride(self):
        print(f"{self.name} is riding.")


# Creating an object named Ronaldo from Elephant class
Ronaldo = Elephants("Ronaldo")
# Calling methods .walk() and .ride() on this object
Ronaldo.walk()
Ronaldo.ride()

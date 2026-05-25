class People:
    def __init__(self, name, gender, birth_year):
        self.name = name
        self.gender = gender
        self.birth_year = birth_year

    def get_age(self):
        current_year = 2026
        user_age = current_year - self.birth_year
        return user_age


# first method
class Player:
    def __init__(self, club, pay):
        self.club = club
        self.pay = pay

    def get_info(self):
        return f"Player plays for {self.club} club."


class Footballer(People, Player):
    def __init__(self, name, gender, birth_year, club, pay, position):
        People.__init__(self, name, gender, birth_year)
        Player.__init__(self, club, pay)
        self.position = position


muller = Footballer("Thomas Muller", "M", 1956, "Bayern", 100000, "ST")
age = muller.get_age()
print(age)

muller_info = muller.get_info()
print(muller_info)


# Another method


class Player(People):
    def __init__(self, name, gender, birth_year, club, pay):
        People.__init__(self, name, gender, birth_year)
        self.club = club
        self.pay = pay

    def get_info(self):
        return f"Player plays for {self.club} club."


class Footballer(Player):
    def __init__(self, name, gender, birth_year, club, pay, position):
        Player.__init__(self, name, gender, birth_year, club, pay)
        self.position = position


muller = Footballer("Thomas Muller", "M", 1956, "Bayern", 100000, "ST")
age = muller.get_age()
print(age)
muller_info = muller.get_info()
print(muller_info)


# Property:- In Python, @property is a built-in decorator that lets you define a method that can be accessed like an attribute.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14 * self.radius**2

circle_area= Circle(5)
print(circle_area.area)

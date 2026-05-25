# Create a class Car with following details:
# Attributes: brand, model, color. Default value of color should be blue.
# Methods: display_info, start_engine, stop_engine.
# display_info should return Brand: {brand}, Model: {model}, Color: {color}.
# start_engine should return "Engine of {self.brand} {self.model} started".
# stop_engine should return "Engine of {self.brand} {self.model} stopped".
# Create two objects of Car class
# car_1 with brand Toyota, model Corolla and color Red.
# car_2 with brand Honda, model Civic.
# Call display_info, start_engine and stop_engine for both objects and display the output.


class Car:
    def __init__(self, brand, model, color="blue"):
        self.brand = brand
        self.model = model
        self.color = color

    # methods
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Color: {self.color}")

    def start_engine(self):
        print(f"Engine of {self.brand} {self.model} started")

    def stop_engine(self):
        print(f"Engine of {self.brand} {self.model} stopped")


# creating objects
car_1 = Car("Toyota", "Corolla", "Red")
car_2 = Car("Honda", "Civic")

# calling methods and displaying output
car_1.display_info()
car_1.start_engine()
car_1.stop_engine()

car_2.display_info()
car_2.start_engine()
car_2.stop_engine()


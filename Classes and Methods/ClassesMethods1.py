class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.speed = 0

    def accelerate(self, amount):
        self.speed += amount

    def brake(self, amount):
        self.speed -= amount
        if self.speed < 0:
            self.speed = 0

    def get_speed(self):
        return self.speed


my_car = Car("Toyota", "Corolla")

my_car.accelerate(20)
print("Speed:", my_car.get_speed())

my_car.brake(10)
print("Speed after braking:", my_car.get_speed())

# Create a car class

# Doors, model, make

# Speed
# Accelerate and brake methods (increase and decrease speed)

# Maximum speed


class Car:

    def __init__(self, name):
        self.doors = 4
        self.name = name
        self.__speed = 0

    def reveal_speed(self):
        return self.__speed

    def acc(self, accel):
        self.__speed += accel
        if self.__speed > 200:
            self.__speed = 200

    def brake(self, brake):
        self.__speed += brake
        if self.__speed < 0:
            self.__speed = 0


new_car = Car("Ferarri")

new_car.acc(300)
print(new_car.reveal_speed())
new_car.brake(-200)
print(new_car.reveal_speed())



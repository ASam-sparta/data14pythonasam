class Animal:
    def __init__(self, name, legs):
        self._hunger = 5
        self.name = name
        self.legs = legs

    def breathe(self):
        print("Breathing in ...")
        print("Breathing out...")
        self._hunger += 0.1

    def eat(self):
        print("Nom nom nom")
        self._hunger = 8


class Mammal(Animal):
    def __init__(self, name, colour):
        super().__init__(name, 4)
        self.colour = colour
    def give_birth(self):
        print("I have produced a child. It is not an egg")


# my_mammal = Mammal()
#
# my_mammal.give_birth()
# my_mammal.breathe()
# print(my_mammal._hunger)


class Dog(Mammal):
    def __init__(self, name, colour):
        super().__init__(name, colour)
    def wag_tail(self):
        print("Swish swish")
        self._hunger += 1


class GoldenRetriever(Dog):
    def bark(self):
        print("Woof!")

# my_dog = Dog("Alex", "Black")
# my_dog.breathe()
# my_dog.give_birth()
# print(f"{my_dog.legs()}")
# my_golRet = GoldenRetriever()
# print(my_golRet.bark())

class Bat(Mammal):
    def __init__(self, name, colour):
        super().__init__(name, colour)
        self.legs = 2

my_bat = Bat("Bruce", "Black")
print(my_bat.legs)


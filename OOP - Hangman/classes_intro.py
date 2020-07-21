# # No spaces in name and capitalize all words
# class GoodDog:
#     # Snake case
#     # This is an attribute (variable)
#     animal_type = "canine"
#
#     # Functions inside classes are called methods (functions)
#     def bark(self):  # self i referring to the current class,
#                      # bark refers to GoodDog
#         return "Woof!"
#
#
# fluffy = GoodDog() # Created instance of class (an Object)
# print(fluffy.animal_type)
# print(fluffy.bark())
#
#
# fido = GoodDog()
# lassie = GoodDog()
# print(fido.animal_type)
# print(lassie.bark())
#
#
# fido.animal_type = "bird"
# print(fido.animal_type)
#
# GoodDog.animal_type = "arachnid"
# print(lassie.animal_type)


# PROPERLY

class Dog:

    animal_kind = "bird"

    def __init__(self, name, colour):  # Initialisation, set at the point
                         # the object is created, if method changes
                         # it does not change this
        self.name = name  # anything you want to change in here
        self.legs = 4
        self.animal_kind = "canine"
        self.colour = colour
        self.__secret = "I can't eat chocolate"

    def bark(self):
        return "WOOF!"

    def intro(self):
        return f"Hello, my name is {self.name}"  # REMEMBER self.name!!

    def reveal_secret(self): # Getter
        return self.__secret

    def set_secret(self, secret):  # SETTER
        self.__secret = secret
# big_dog = Dog()
#
# small_dog = Dog()
#
# print(big_dog.name)
# print(small_dog.legs)
# print(big_dog.animal_kind)
#
# print("-----HORRIBLE CURSE------")
# Dog.animal_kind = "arachnid"
# Dog.legs = 8
#
# print(big_dog.animal_kind)
# print(big_dog.legs)


new_dog = Dog("Pablo", "White") # Instantiation - upon creating a new object
print(new_dog.intro())
print(new_dog.set_secret("Hi"))


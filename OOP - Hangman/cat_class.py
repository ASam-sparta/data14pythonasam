# A cat class

# Attributes hidden: which of these change depending on method
# Mood
# Hunger
# Energy

# Methods
# Sleep
# Play
# Feed

# Hidden method
# Meow
# Think which methods call meow


class Cat:

    def __init__(self):
        self._mood = 5
        self._hunger = 5
        self._energy = 5

    def sleep(self):
        self._energy += 8
        if self._energy >= 10:
            self._energy = 10
        self._mood += 2
        if self._mood >= 10:
            self._mood = 10
        self._hunger -= 5
        if self._hunger <= 0:
            self._hunger = 0
            self._meow()

    def play(self):
        self._mood += 3
        if self._mood >= 10:
            self._mood = 10
        self._hunger -= 3
        if self._energy >= 10:
            self._energy = 10
        elif self._energy <= 0:
            self._energy = 0
            self._meow()
        self._energy -= 5
        if self._energy <= 0:
            self._energy = 0
            self._meow()

    def feed(self):
        self._hunger += 5
        if self._energy >= 10:
            self._energy = 10
        self._mood += 6
        if self._mood >= 10:
            self._mood = 10
        self._energy += 4
        if self._energy >= 10:
            self._energy = 10

    def _meow(self):
        print("Meow")

    def cat_values(self):
        return f"Hunger {self._hunger}, Mood {self._mood}, Energy {self._energy}"

new_cat = Cat()
print(new_cat.play())
print(new_cat.cat_values())

# Encapsulation is for within the class, hiding functionality from the user
# Set distinction between private and public attributes and methods
# Opposite is public

# Abstraction - abstracting away granular details to make life easier
# Very clear inputs and outputs for public, shouldn't have to fix or
# know the mechanisms

# example of toaster is we cannot change the temperature of toaster,
# this is controlled by toaster



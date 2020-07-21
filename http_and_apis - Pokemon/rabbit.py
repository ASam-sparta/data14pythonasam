from time import sleep
from random import randint

class Rabbit:
    def __init__(self):
        self.months = 0
        self.pregnant_rabbits = 1
        self.males = 1
        self.females = 1
        self.female_dict = {"female": 1, "newborns": "matured_females": 1, "pregnant_female": self.pregnant_rabbits}
        self.male_dict = {"male": 1}

    def advance_time(self, months=None):
        sleep(1)
        if not months:
            months = self.months
        months += 1
        self.months = months
        return months
    #
    # def number_of_babies(self):
    #     sum = 0
    #     for i in range(self.pregnant_rabbits):
    #         num_babies = randint(1, 14)
    #         sum += num_babies
    #     return sum

    # def gender_of_babies(self):
    #     num_babies = self.number_of_babies()
    #     male_sum = 0
    #     female_sum = 0
    #     for i in range(num_babies):
    #         gender = randint(1, 2)
    #         if gender == 1:
    #             male_sum += 1
    #         elif gender == 2:
    #             female_sum += 1
    #     return male_sum, female_sum


    def rabbit_generator(self):
        sum = 0
        male_sum = 0
        female_sum = 0
        for i in range(self.pregnant_rabbits):
            num_babies = randint(1, 14)
            sum += num_babies
            self.female_dict["pregnant_female"] -= 1
        for i in range(sum):
            gender = randint(1, 2)
            if gender == 1:
                male_sum += 1
            elif gender == 2:
                female_sum += 1
        self.male_dict["male"] += male_sum
        self.female_dict["female"] += female_sum
        return sum, male_sum, female_sum

xyz = Rabbit()
# print(xyz._set_initial())
# print(xyz.advance_time(3))
print(xyz.rabbit_generator())
print(xyz.male_dict)
print(xyz.female_dict)

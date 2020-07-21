from random import randint
from time import sleep


class Rabbits:
    def _init_(self):
        self.lifespan = 60
        self.babies_per_pregnancy = [1, 14]  # [max_births, min_births]
        self.male_ages = {3: 1}  # {months_old: count}
        self.female_ages = {3: 1}
        self.pregnant_count = [0]
        self.total = 2
        self.male_total = 1
        self.female_total = 1
        self.new_babies = 0
        self.new_deaths = 0
        self.month_total = 0
        self.year_total = 0

    def _pregnancies(self, mature_male_count=None, mature_female_count=None,
                     non_pregnant_female=None, male_ages=None,
                     female_ages=None):
        # Determines the number of pregancies in a month
        if not male_ages:
            male_ages = self.male_ages
        if not female_ages:
            female_ages = self.female_ages
        if not mature_male_count:
            mature_male_count = 0
            for key in male_ages:
                if key >= 3:
                    mature_male_count += male_ages[key]
        if not mature_female_count:
            mature_female_count = 0
            for key in female_ages:
                if key >= 3:
                    mature_female_count += female_ages[key]
        if not non_pregnant_female:
            non_pregnant = mature_female_count - self.pregnant_count[0]
        new_pregnancies = min(mature_male_count, non_pregnant)
        self.pregnant_count.append(new_pregnancies)
        return new_pregnancies

    def _births(self, birthing_females=None):
        # Finds the number of rabbits that are born
        number_born = 0
        if not birthing_females:
            birthing_females = self.pregnant_count.pop(0)
        for birth in range(0, birthing_females):
            min_births = self.babies_per_pregnancy[0]
            max_births = self.babies_per_pregnancy[1]
            number_born += randint(min_births, max_births)
        self.new_babies = number_born
        self.total += number_born
        return number_born

    def _assign_gender(self, babies=None):
        # Sets the gender of the babies at birth
        if not babies:
            babies = self.new_babies
        males = randint(0, babies)
        females = babies - males
        self.male_ages[0] = males
        self.male_total += males
        self.female_ages[0] = females
        self.female_total += females
        male_ages = {0: males}
        female_ages = {0: females}
        self.male_ages[0] = males
        self.female_ages[0] = females
        return [male_ages, female_ages]

    def _get_deaths(self, male_deaths=None, female_deaths=None, total=None,
                    male_total=None, female_total=None):
        # Find the number of rabbits that have died of each gender
        if not male_deaths:
            try:
                male_deaths = self.male_ages[60]
            except KeyError:
                male_deaths = 0
        if not female_deaths:
            try:
                female_deaths = self.female_ages[60]
            except KeyError:
                female_deaths = 0
        if not total:
            total = self.total
        if not male_total:
            male_total = self.male_total
        if not female_total:
            female_total = self.female_total
        deaths = male_deaths + female_deaths
        try:
            self.male_ages[60] = 0
        except KeyError:
            self.male_ages = self.male_ages
        try:
            self.female_ages[60] = 0
        except KeyError:
            self.female_ages = self.female_ages
        male_total -= male_deaths
        female_total -= female_deaths
        total -= deaths
        self.female_total = female_total
        self.male_total = male_total
        self.total = total
        self.new_deaths = deaths
        return [female_total, male_total, total, deaths]

    def _change_ages(self, male_ages=None, female_ages=None):
        # Changes the ages of all living rabbits
        if not male_ages:
            male_ages = self.male_ages
        if not female_ages:
            female_ages = self.female_ages
        new_male = {}
        new_female = {}
        for key in male_ages:
            new_male[key + 1] = male_ages[key]
        male_ages = new_male
        self.male_ages = male_ages
        for key in female_ages:
            new_female[key + 1] = female_ages[key]
        female_ages = new_female
        self.female_ages = female_ages
        return [male_ages, female_ages]

    def _print_to_user(self, male_total=None, female_total=None, births=None,
                       deaths=None, months=None, years=None, pregnancies=None):
        # Prints relevant information to user
        if not male_total:
            male_total = self.male_total
        if not female_total:
            female_total = self.female_total
        if not births:
            births = self.new_babies
        if not deaths:
            deaths = self.new_deaths
        if not months:
            months = self.month_total
        if not years:
            years = self.year_total
        if not pregnancies:
            pregnancies = self.pregnant_count[0]
        pop_change = births - deaths
        print(f"\n\n\n --- {years} years, {months} months --- \n")
        print(f"Births this month: {births}")
        print(f"Deaths this month: {deaths}")
        if pop_change > 0:
            print(f"The population increased by {pop_change} this month")
        elif pop_change < 0:
            print(f"The population decreased by {pop_change * -1} this month")
        else:
            print(f"The population remained the same this month")
        print(f"New Population: {male_total + female_total}")
        print(f"This includes {male_total} males and {female_total} females")
        if pregnancies == 1:
            print(f"There was {pregnancies} new pregnancy this month")
        elif pregnancies == 0:
            print("There were no new pregnancies this month")
        else:
            print(f"There were {pregnancies} new pregnancies this month")

    def advance_time(self):
        sleep(1)
        self._pregnancies()
        self._births()
        self._assign_gender()
        self._get_deaths()
        self._change_ages()
        self.month_total += 1
        if self.month_total == 12:
            self.month_total = 0
            self.year_total += 1
        self._print_to_user()


testing = Rabbits()
testing.advance_time()
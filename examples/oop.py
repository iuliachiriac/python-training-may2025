from datetime import date


class Person:
    MIN_YEAR = 1900
    count = 0  # class variable

    def __init__(self, name, date_of_birth: date):
        self.name = name  # instance variable
        self.date_of_birth = date_of_birth
        self._increment_count()

    @property
    def date_of_birth(self):  # getter
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, value: date):  # setter
        if value.year < self.MIN_YEAR:
            raise ValueError(
                f"Invalid date of birth (year should be <= {self.MIN_YEAR})")
        self._date_of_birth = value

    @property
    def age(self):
        return self.years_since(self._date_of_birth)

    def greet(self, greeting):  # instance method
        print(f"{greeting.capitalize()}! I am {self.name}!")

    def add_last_name(self, last_name):
        self.name = f"{self.name} {last_name}"

    @classmethod
    def _increment_count(cls):  # class method
        cls.count += 1

    @staticmethod
    def years_since(date_obj: date):
        today = date.today()
        years = today.year - date_obj.year
        if (today.month, today.day) < (date_obj.month, date_obj.day):
            years -= 1
        return years

    def __str__(self):
        return f"<name='{self.name}' date_of_birth='{self._date_of_birth}'>"

    def __repr__(self):
        return f"<{self.__class__.__name__} object name={repr(self.name)} "\
               f"date_of_birth={repr(self._date_of_birth)}>"

    def __lt__(self, other):
        return self._date_of_birth > other.date_of_birth

    def __le__(self, other):
        return self._date_of_birth >= other.date_of_birth


if __name__ == "__main__":
    p1 = Person("Anna", date(1986, 1, 13))
    p2 = Person("Mike", date(2001, 6, 24))
    print(p1, p2, p1.name, p2.name, p1.date_of_birth, p2.date_of_birth)
    print(Person.count, p1.count, p1.count is Person.count)

    p1.add_last_name("Smith")

    p1.greet("hi")
    p2.greet("hello")

    print("Anna is younger than Mike:", p1 < p2)
    print("Anna is older than Mike:", p1 >= p2)

    person_list = [p1, p2, Person("John", date(1995, 8, 3))]
    person_list.sort()
    print(person_list)

    # If comparison was not supported by Person objects,
    # we could sort them by date_of_birth
    person_list.sort(key=lambda person: person.date_of_birth, reverse=True)
    print(person_list)

    print(Person.years_since(date(1995, 12, 25)))

    print(p1.date_of_birth)
    try:
        p1.date_of_birth = date(1887, 1, 13)
    except ValueError as ex:
        print(ex)
    print(p1.date_of_birth)
    # del p1.date_of_birth

    try:
        p3 = Person("Jane", date(1895, 8, 3))
    except ValueError as ex:
        print(ex)

    print(f"{p1.name} is {p1.age} years old.")

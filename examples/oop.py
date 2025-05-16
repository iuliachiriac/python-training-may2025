import random
from datetime import date


class InvalidDateException(Exception):
    pass


class Person:
    MIN_YEAR = 1900
    count = 0  # class variables

    def __init__(self, p_name, date_of_birth: date = None):
        self.name = p_name  # instance variables
        self.date_of_birth = date_of_birth
        self._increment_count()

    def greet(self, greeting: str):  # instance method
        print(f"- {greeting.capitalize()}! I am {self.name}.")

    @classmethod
    def _increment_count(cls):  # class method
        cls.count += 1

    @staticmethod
    def years_since(date_start: date):  # static method
        today = date.today()
        years = today.year - date_start.year
        if (date_start.month, date_start.day) > (today.month, today.day):
            years -= 1
        return years

    @property
    def age(self):  # computed attribute
        return self.years_since(self._date_of_birth)

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, value: date):
        if value.year < self.MIN_YEAR:
            raise InvalidDateException(f"Year should be >= {self.MIN_YEAR}")
        self._date_of_birth = value

    def __str__(self):
        return f"{self.__class__.__name__}(name={self.name}, dob={self._date_of_birth})"

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other: "Person"):
        return self._date_of_birth > other.date_of_birth

    def __le__(self, other: "Person"):
        return self._date_of_birth >= other.date_of_birth


class Student(Person):
    def __init__(self, name, date_of_birth, university):
        super().__init__(name, date_of_birth)
        self.university = university

    def greet(self):
        print(f"- Hello! I am {self.name} and I study at {self.university}.")

    def get_grade(self, subject):
        return random.randint(3, 10)


if __name__ == "__main__":
    p1 = Person("Anna", date(2002, 4, 1))
    p2 = Person("Jane", date(1984, 7, 15))
    p3 = Person("Mike", date(1992, 12, 30))

    p1.greet("hi")
    p2.greet("hello")

    print(p1.name, p2.name, p3.name)
    print(p1.date_of_birth)

    print(p1, str(p1))

    print("Person count:", Person.count, p1.count, p1.count is Person.count)

    persons = [p1, p2, p3]
    persons.sort()
    print(persons)

    if p2 >= p1:
        print(f"{p2.name} is older than {p1.name}.")

    # Person._Person__increment_count()
    # Person._increment_count()
    # print(dir(Person))
    # print(Person.count)

    print(Person.years_since(date(1989, 12, 25)))
    print(f"{p1.name} is {p1.age} years old.")
    try:
        p4 = Person("John", date(1890, 1, 5))
    except InvalidDateException as ex:
        print(ex)
    try:
        p1.date_of_birth = date(1890, 1, 5)
    except InvalidDateException as ex:
        print(ex)
    print(p1.age)

    s1 = Student("Sally", date(2004, 5, 17), "MIT")
    print(s1)
    print(f"{s1.name} is {s1.age} years old.")
    s1.greet()
    subject = "Maths"
    print(f"{s1.name} got a {s1.get_grade(subject)} in {subject}.")

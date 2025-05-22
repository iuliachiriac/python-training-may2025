from datetime import date


class Person:
    count = 0  # class variable

    def __init__(self, name, date_of_birth):
        self.name = name  # instance variable
        self.date_of_birth = date_of_birth
        Person.count += 1

    def greet(self, greeting):
        print(f"{greeting.capitalize()}! I am {self.name}!")

    def add_last_name(self, last_name):
        self.name = f"{self.name} {last_name}"


if __name__ == "__main__":
    p1 = Person("Anna", date(1986, 1, 13))
    p2 = Person("Mike", date(2001, 6, 24))
    print(p1, p2, p1.name, p2.name, p1.date_of_birth, p2.date_of_birth)
    print(Person.count, p1.count, p1.count is Person.count)

    p1.add_last_name("Smith")

    p1.greet("hi")
    p2.greet("hello")

from datetime import date


class Person:
    count = 0  # class variables

    def __init__(self, p_name, date_of_birth=None):
        self.name = p_name  # instance variables
        self.date_of_birth = date_of_birth
        Person.count += 1

    def greet(self, greeting: str):
        print(f"- {greeting.capitalize()}! I am {self.name}.")

    def __str__(self):
        return f"Person(name={self.name}, dob={self.date_of_birth})"

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other: "Person"):
        return self.date_of_birth > other.date_of_birth

    def __le__(self, other: "Person"):
        return self.date_of_birth >= other.date_of_birth


if __name__ == "__main__":
    p1 = Person("Anna", date(2002, 4, 1))
    p2 = Person("Jane", date(1984, 7, 15))
    p3 = Person("Mike", date(1992, 12, 30))

    p1.greet("hi")
    p2.greet("hello")

    print(p1.name, p2.name, p3.name)
    print(p1.date_of_birth)

    print(p1, str(p1))

    print(Person.count, p1.count, p1.count is Person.count)

    persons = [p1, p2, p3]
    persons.sort()
    print(persons)

    if p2 >= p1:
        print(f"{p2.name} is older than {p1.name}.")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)  
        self.subject = subject
        self.salary = salary

    def display(self):
        self.display_person()  
        print("Subject:", self.subject)
        print("Salary:", self.salary)


def main():
    print("Enter Teacher Details:")
    name = input("Name: ")
    age = int(input("Age: "))
    subject = input("Subject: ")
    salary = float(input("Salary: "))

    obj1 = Teacher(name, age, subject, salary)

    print("\n--- Teacher Information ---")
    obj1.display()


if __name__ == "__main__":
    main()

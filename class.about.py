'''
    (1) What is class
    (2) ordinary vs static properties
    (3) special methods
'''
print("===== What is class =====")
# class - blueprint for object creation!
# structure > state - constructor - method


class Person:
    # state
    # message = "class state property"
    message = "static state property"

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

        # method
    def introduce(self):
        print(f"{self.name} says: How do you do!")

    def say_age(self):
        print(f"{self.name} says: I am {self.age} years old")

    @classmethod
    def explain(cls):
        print("Class: static method property executed!")


person1 = Person("Justin", 25)
person2 = Person("Martin", 35)
person3 = Person("John", 22)

# ordinary state property (name, age)
# name = person1.name
print("person1.name:", person1.name)

# ordinary method property

person1.introduce()
person2.say_age()

# ordinary state and methods live with objects
# static properties are directly belonging to classes and live with classes

print("===== ordinary vs static properties =====")

# static state

new_message = Person.message
print("new_message:", new_message)

# static method
Person.explain()

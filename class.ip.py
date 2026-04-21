''' CLASS deep diving
  (1) Encapsulation
  (2) Inheritence <
  (3) Polimorphism <
'''

print("===== INHERITENCE =====")
# PARENT > CHILD
# parent only provide public & protected properties (state + method) to children!


class Animal:  # parent
    # state
    description = "This class is parent for animals"

    # constructor
    def __init__(self, voice):
        self._status = "animal is alive"
        self.voice = voice

    # method
    def make_voice(self):
        print(f"the animal can make voice: {self.voice}")


class Dog(Animal):  # child
    # state

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def protect(self):
        print("Yes, I can protect you!")


class Cat(Animal):  # child
    # state

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def play(self):
        print("Yes, I can play with you!")


class Fish(Animal):  # child
    # state

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def protect(self):
        print("Yes, I can swim!")


dog = Dog("Rex", "wow", True)
cat = Cat("Tom", "myeow", True)
fish = Fish("Nemo", "ZzZ", False)

dog.introduce()
cat.introduce()
fish.introduce()

print("------------------")
dog.make_voice()
fish.make_voice()

print("------------------")
print(Animal.description)
print(dog.description)

print(dog.voice, fish.voice)
print("dog.status:", dog._status)
print("cat.status:", cat._status)

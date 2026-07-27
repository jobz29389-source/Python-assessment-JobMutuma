"""Task 6: Object-Oriented Python"""

class Animal:
    species = "Unknown"
    counter = 0

    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
        self.__age = 0  # private attribute
        Animal.counter += 1

    def speak(self):
        print(f"{self.name} says {self.sound}")

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age >= 0:
            self.__age = age

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks: Woof!")

a1 = Animal("Cat", "Meow")
a2 = Animal("Cow", "Moo")
a1.speak()
a2.speak()

d1 = Dog("Rex", "Woof")
d1.speak()

d1.set_age(3)
print(d1.get_age())

print("Total animals created:", Animal.counter)
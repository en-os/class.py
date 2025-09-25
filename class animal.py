
class Animal:
    def move(self):
        return "Animal moves"

class Bird(Animal):
    def move(self):
        return "Flying high!"

class Fish(Animal):
    def move(self):
        return "Swimming deep!"

class Dog(Animal):
    def move(self):
        return "Running fast!"

class Snake(Animal):
    def move(self):
        return " Slithering silently!"

# Test
animals = [Bird(), Fish(), Dog(), Snake()]
for animal in animals:
    print(animal.move())

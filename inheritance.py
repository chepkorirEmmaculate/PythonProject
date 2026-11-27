
class Animal:
    isMammal = True
    age = 7
    def movement(self):
        print("Animal is moving")


#Child class/Sub Class/Derived Class
class Dog(Animal):
    def bark(self):
        print("Woof!! Woof!! Woof!!")

class Cat(Animal):
    def meow(self):
        print("Meow!! Meow!!")

dog1 = Dog()
dog1.movement()
print(dog1.isMammal)
print(dog1.age)


cat1 = Cat()
cat1.meow()
print(cat1.isMammal)
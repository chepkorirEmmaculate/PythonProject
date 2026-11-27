#Class is a blueprint of an object.
#Object is an instance of a class.


class Employee:

    def __init__(self, name, gender, position, age):
        self.name = name
        self.gender = gender
        self.position = position
        self.age = age

    #name = "John"
    #gender = "Male"
    #position = "Managing Director"
    #age = 56

    def drive(self):
        print("Employee is driving.")

    def eat(self):
        print("Employee is eating.")

employee1 = Employee("Mark", "Male","CEO",57) #Creating an object
print(employee1.name, employee1.gender, employee1.position)
employee1.drive()


employee2 = Employee("Diana", "Female", "Manager", 36)
print(employee2.name, employee2.gender, employee2.position)
employee2.drive()
employee2.eat()


employee3 = Employee("Dennis", "Male", "Receptionist", 41)
print(employee3.name, employee3.gender, employee3.position)
employee3.drive()
employee3.eat()
# module in python is just a file that contains python code with .py extension

# generally you do not want your module to do anything when it is imported
# you just want the module to define things like variables, functions, classes..
# print("Start of my_module.py")

my_variable = 10
my_string = "RTU"
my_list = [1, 2, 3, 4, 5]

def my_addition(a, b):
    return a + b

# i could even have a class let's a Person class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Person created")

    # __str__ method
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

# again we do not want to have print statement here when imported
# print("End of my_module.py")

# we can use this module in my_program.py or any other program
# but also we can use this module as a standalone program

# how? we use so called main guard
# we use an if statement to check if this module is being run as a standalone program

if __name__ == "__main__":
    print("This is my_module.py being run as a standalone program")
    print("We can use this for testing purposes")
    print(my_variable)
    print(my_string)
    print(my_list)
    print(my_addition(10, 20))
    alice = Person("Alice", 20)
    bob = Person("Bob", 30)
    print(alice)
    print(bob)
    print(alice.get_name())
    print(alice.get_age())
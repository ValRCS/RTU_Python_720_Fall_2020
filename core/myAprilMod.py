## Some Commonly used functions
## so a regular python code file with extension .py is a module

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

# I could define constants here
# of course Python does not have true constants
MYPI = 3.14
some_text = "Hello darkness my old friend"


# I could define a class here
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
    
# let's add   main guard for testing

if __name__ == "__main__":
    print("This is myAprilMod.py being run as a standalone program")
    print("We can use this for testing purposes")
    print(add(10, 20))
    print(sub(20, 10))
    alice = Person("Alice", 20)
    bob = Person("Bob", 30)
    print(alice)
    print(bob)
    print(alice.get_name())
    print(alice.get_age())
    print(MYPI)
    print(some_text)
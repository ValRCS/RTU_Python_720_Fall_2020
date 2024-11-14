# this will serve as my main program
# we will want to include/import the module we create
# this is different from standard in a way that it is created by you not by python itself

# Advantages of using modules
# 1. Code reusability
# 2. Code organization
# 3. Easy to maintain
# 4. Easy to share with others
# 5. Namespacing - less chance of naming conflicts

# let's import my_module.py

import my_module # this will also create cache file my_module.cpython-3XX.pyc XX is version
# here I can start using whatever is in my_module.py

print(my_module.my_variable)
print(my_module.my_string)
print(my_module.my_list)

# i can my functions
print(my_module.my_addition(10, 20))

# i can create objects from the class in my_module.py
alice = my_module.Person("Alice", 20)
bob = my_module.Person("Bob", 30)

# where does Python look for modules?
# let's use sys module to find out
import sys # this is standard library module usually we put imports up top
print(f"Paths where python looks for modules: {sys.path}")

# so Python looks for modules in the current directory, standard library, and other directories
# therefore you should name your modules differently from standard library modules
# check the list of standard library modules from https://docs.python.org/3/library/

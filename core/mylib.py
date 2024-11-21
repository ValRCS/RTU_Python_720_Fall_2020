# this is a small .py file that we will use for as a module(import)
import math # importing standard Python math library
MY_PI = 3.1415926

def nb_year(pop_start, percent, yearly_arrival, pop_end):
    count = 0
    population = pop_start
    while population < pop_end:
        # short hand population *= (1+percent/100)
        # also shortone population += population * percent / 100
        population = population + math.floor(population * percent / 100)
        population += yearly_arrival
        count += 1
    return count

def add(a,b):
    return a+b

# could add main guard here

"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
import math 

def primes(number_of_primes):
    list = []
    count = 2
    
    while len(list)<number_of_primes:
        isprime = True
        
        for x in range(2, int(math.sqrt(count) + 1)):
            if count % x == 0: 
                isprime = False
                break
        
        if isprime:
            list.append(count)
        
        count += 1
    return list

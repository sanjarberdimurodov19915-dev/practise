'''
    (1) What is object
    (2) Iterable objects & RANGE
    (3) DICTIONARY
    (4) Error handling system
'''

import array  # package / module
import math  # package
from math import ceil, asin
print("===== What is object =====")
# An object has state and method properties.
# Everyting is object in Python!

print(type('Hello world'))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

# a = 97.7
# result1 = math.ceil(a)
# print(result1)

# Paradigm > Functional Programming & OOP
# OOP 4 CONCEPTS > Abstraction | Encapsulation | Inheritence | Polimorphism
result1 = math.ceil(97.7)  # CALL
print("result1:", result1)

result2 = ceil(98.7)
print("result2:", result2)

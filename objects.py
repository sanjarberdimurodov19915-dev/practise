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

print("===== Error handling system =====")

car_dict = dict(name="Tayota", year="2026", electric=True)

try:
    print("passed here")
    a = car_dict.speed
    result = car_dict["origin"]
    # result = car_dict["year"]
    print("result:", result)

    # pass

except Exception as err:
    print("General Error:", err)

# except (KeyError, AttributeError) as err:
   # print("Error:", err)

# except KeyError as err:
    # print("No origin state property found:", err)
    # pass
# except AttributeError as err:
    # print("No speed found:", err)

else:
    print("Executed succesfully without errors")
finally:
    print("Final closing logic")


# result = car_dict["origin"]
# print("result:", result)

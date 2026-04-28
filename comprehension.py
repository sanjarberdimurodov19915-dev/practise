''' Comprehension
    (1) What is comprehension & list comprehension
    (2) set and dictionary comprehension
'''

print("====== What is comprehension & list comprehension ======")
# Comprehension acts like spread operator!

''' Comprehension general syntax:
    a) *iterable
    b) <expression> for item in iterable
    c) <expression> for item in iterable <condition>
'''

# list comprehension
numbers = [1, 2, 4, 2, 1, 20]
list_numbers = [*numbers]  # a version
# list_numbers = numbers
print("list_numbers:", list_numbers)
print(numbers is list_numbers)
print(id(numbers), id(list_numbers))

people = [("Robert", 21), ("Steve", 19), ("Tony", 25)]
list_people = [person[0] for person in people]  # b version
# list_people = [person[1] for person in people]
print("list_people:", list_people)

cars = [
    ("Ferrari", 78),
    ("Tayota", 87),
    ("Audi", 116),
    ("BMW", 109),
    ("Paganit", 33)
]
list_cars = [car[0] for car in cars if car[1] > 80]  # c version
print("list_cars:", list_cars)

print("====== set and dictionary comprehension ======")

numbs = [1, 5, 4, 20, 4, 5, 1, 4]
set_numbs = {*numbs}  # a version
print("set_numbs:", set_numbs)

dict_people = {person[0]: person[1] for person in people}  # b version
print("dict_people:", dict_people)

dict_people2 = {person[0]: person[1]
                for person in people if person[1] > 20}  # c version
print("dict_people2:", dict_people2)

# generic typeni ushbu b - version (<expression> for item in iterable) orqali hosil qilish mumkin
# generic typelar katta miqdordagi sonlar bilan ishlashda ishlatiladi

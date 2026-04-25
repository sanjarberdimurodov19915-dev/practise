''' List
    (1) Working with lists
    (2) List methods
    (3) Lambda function
    (4) enumerate, map and filter

'''

print("========== Working with lists ==========")
# Java/PHP/NodeJS array => Python list

# literal
person = {"name": "Sanjar", "age": 25}  # dictionaryni literal usulda qurish
people = ("Andrew", "John", "Michael")  # tupleni literal usulda qurish
groups = ["MIT", "FLEXY", "DEVEX", "MG"]  # listni literal usulda qurish
for team in groups:
    print(f"the team: {team}")

# cinstructor
letters = list("Hello world!")
print(f"the letters: {letters} and size: {len(letters)}")

print("------------------")
fruits = ["apple", "orange", "lemon", "kiwi"]

a = fruits[0]
b = fruits[0:2]  # [0, 2)
c = fruits[::3]  # 1 qiymatni oladi va -
# - keyingi qanday sonni kiritsak shuncha sakrab undan keyingi sonni oladi
d = fruits[::-1]

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)

print("========== List methods ==========")
# listni methods > append(), insert(), pop(), remove(), clear(), sort(), index()
# mutable - append(), insert(), pop(), remove(), clear(), sort()
# immutable - index()

letters = ["a", "d", "b"]

letters.append("c")  # list oxiridan qo'shish
print(f"the append result: {letters}")

letters.insert(0, "z")  # list boshidan qo'shish
print(f"the insert result: {letters}")

size = len(letters) - 1
result1 = letters.pop(size)  # oxiridan ajratib olish
print(f"the pop result1: {result1} and letters: {letters}")

result2 = letters.pop(0)  # boshidan ajratib olish
print(f"the pop result2: {result2} and letters: {letters}")

print("--------------------")
animals = ["dog", "cat", "capybara", "fish", "lion"]
print("animals:", animals)

animals.remove("lion")
print("animals remove", animals)

del animals[2: 4]
print("animals delete:", animals)

exist = animals.index("cat")  # element mavjud bo'lsa index raqamini qaytaradi
print("cat exist:", exist)       # mavjud bo'lmasa value error qaytaradi

animals.clear()
print("animals clear:", animals)

# exist2 = animals.index("cat") # bu holda indexni olib bo'lmaydi
# print("exist2:", exist2)
# shuning uchun errorni
if "cat" in animals:
    print("index of cat:", animals.index("cat"))
else:
    print("cat does not exist")

print("--------------------")
numbers = [2, 20, 12, 8, 57]
numbers.sort()
print("sort default numbers:", numbers)
numbers.sort(reverse=True)
print("sort reverse:", numbers)

# immutable sort amalini hosil qilmoqchi bo'lsak sorted functionidan foydalanamiz
numbs = [2, 20, 12, 100]
new_numbs = sorted(numbs)
print(f"the sorted numbs: {numbs} and new_numbs: {new_numbs}")

print("========== Lambda function ==========")
# lambda is small anonymous function!
def calculate(x, y): return x*y


result = calculate(3, 5)
print("result:", result)

people = [
    ("Robert", 20),
    ("Steve", 19),
    ("Joseph", 25),
    ("Michael", 30),
    ("Ali", 40)
]
people.sort()
print("people(1):", people)

# sorted by age via lambda
people.sort(key=lambda person: person[1])
print("people(2):", people)

print("========== enumerate, map and filter ==========")
# enumerate for index & value

animals = ["dog", "cat", "fish"]  # list
for element in animals:
    print("element:", element)

for element in enumerate(animals):
    print("element:", element)
# yoyish uchun
for (index, value) in enumerate(animals):
    print(f"the index: {index} and value: {value}")

# similar in dictionary
car_obj = dict(brand="Ferrari", year=2025)
result1 = car_obj.get("brand")
print(result1)

print("--------------------")
car_obj = dict(brand="Ferrari", year=2025)
result2 = car_obj.items()
print(result2)
for (key, value) in result2:
    print(f"the key: {key} and value: {value}")

print("--------------------")
# map
cars = [
    ("Ferrari", 78),
    ("Tayota", 87),
    ("Audi", 116),
    ("BMW", 109),
    ("Paganit", 33)
]

# new_cars = []
# for car in cars:
#     new_cars.append(car[0])
# print("new_car(1):", new_cars)

# using map
result_map = map(lambda car: car[0], cars)
print(f"the result1: {result_map} and type: {type(result_map)}")
new_cars = list(result_map)
print("new_cars(2):", new_cars)

print("--------------------")
# filter
result_filter = filter(lambda car: car[1] > 80, cars)
print(f"the result_filter: {result_filter} and type: {type(result_filter)}")
print(list(result_filter))

''' List
    (1) Working with lists
    (2) List methods
    (3) Lambda function
    (4) enumarate, map and filter

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

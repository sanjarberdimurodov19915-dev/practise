''' Array & Set
    (1) Array
    (2) Set
    (3) Specific operators with set
'''
from array import array
print("=========== Array ===========")


# juda katta hajmdagi sonlar bilan ishlash kerak bo'lsa array bilan hosil qilamiz
# i integer float unicode lardan tashkil topgan arraylar hosil qilish mumkin

numbers = array("i", [1, 4, 5, 7, 8, 41])
print("numbers1:", numbers)

numbers.append(100)
numbers.insert(0, 14)
print("numbers2:", numbers)

numbers.remove(5)
numbers.pop()
print("numbers3:", numbers)

del numbers[0:2]
print("numbers4:", numbers)

print("=========== Set ===========")

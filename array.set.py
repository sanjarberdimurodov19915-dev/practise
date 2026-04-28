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
# set is unique collection without keeping order!
new_numbers = array("i", [1, 4, 7, 5, 7, 5, 4, 7, 8, 4, 41])
numbs_set = set(new_numbers)

print("numbs_set:", numbs_set)
print(f"the numbs_set: {numbs_set} and type: {type(numbs_set)}")

numbs_set.add(200)
print("numbs_set1:", numbs_set)

numbs_set.add(7)
print("numbs_set2:", numbs_set)

print("=========== Specific operators with set ===========")
# BITWISE OPERATORS: | & - ^

a = {10, 20, 50}
b = {20, 40}

result1 = a | b  # union - har ikkalasida mavjud bo'lgan barcha sonlardan hosil bo'lgan setni tashkil qiladi
print("result1:", result1)

result2 = a & b  # intersection - har ikkalasida ham mavjud bo'lgan bir xil sonlardan set hosil qiladi
print("result2:", result2)

result3 = a - b  # difference
print("result3:", result3)

result4 = a ^ b  # symmetric difference - bir xillarini tashlab yuboradi
print("result4:", result4)

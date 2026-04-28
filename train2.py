''' List
    (1) Working with lists
    (2) List methods
    (3) Lambda function
    (4) enumerate, map and filter

'''


def get_reverse(word):
    new_word = ""
    for i in word:
        new_word = i + new_word
    return new_word


print(get_reverse("sam"))


# literal

# animals = ["lion", "horse", "fish"]
# print(animals)

# new_numbs = (2, 4, 5, 8, 10)
# print(new_numbs)

# # constructor

# numbers = list("Hello John")
# print(numbers)


print("========== List methods ==========")
# listni methods > append(), insert(), pop(), remove(), clear(), sort(), index()
# mutable - append(), insert(), pop(), remove(), clear(), sort()
# immutable - index()

# animals = ["lion", "horse", "fish"]
# print(animals)

# animals.append("bear")
# print(animals)

# animals.insert(2, "deer")
# print(animals)

# result = animals[-1]
# print(result)

# print(len(animals))

# animals.pop()
# print(animals)

# animals.remove(animals[0])
# print(animals)

# products = ["sut", "qaymoq", "qatiq", "non", "shakar"]
# # print("Bugungi bozorlik")
# # for (index, value) in enumerate(products):
# #     print(f"{index+1} -chi maxsulot: {value}")

# # print("======================")

# # print("Bugungi bozorlik")
# # count = 0
# # for value in products:
# #     if count <= len(products):
# #         count += 1
# #         print(f'{count}-chi maxsulot: {value}')

# result1 = list(filter(lambda value: len(value) > 3, products))
# print(result1)

# result2 = list(map(lambda letter: letter.upper(), products))
# print(result2)

# products = ["sut", "qaymoq", "qatiq", "non", "shakar"]
# print("Bugungi bozorlik")
# new_product = str(input("Mahsulot qo'shing! "))
# products.append(new_product)
# for (index, value) in enumerate(products):
#     print(f"{index+1} -chi maxsulot: {value}")


# a = {10, 20, 50, 60, 80}
# b = {20, 40, 6}

# result1 = a | b  # union - har ikkalasida mavjud bo'lgan barcha sonlardan hosil bo'lgan setni tashkil qiladi
# print("result1:", result1)

# result2 = a & b  # intersection - har ikkalasida ham mavjud bo'lgan bir xil sonlardan set hosil qiladi
# print("result2:", result2)

# result3 = a - b  # difference
# print("result3:", result3)

# result4 = a ^ b  # symmetric difference - bir xillarini tashlab yuboradi
# print("result4:", result4)

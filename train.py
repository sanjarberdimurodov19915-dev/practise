'''
MITASK-O

Savol: Shunday function yozing, u har xil valuelardan iborat array qabul qilsin va List ichidagi sonlar yigindisini hisoblab 
chiqqan javobni qaytarsin.
MASALAN: calculate_summary([10, "10", {son: 10}, true, 35]) return 45
'''
# Masalaning yechimi:


def calculate_summary(arr):
    total = 0
    for item in arr:
        if isinstance(item, (int, float)) and not isinstance(item, bool):
            total += item
    return total


print(calculate_summary([10, "10", {"son": 10}, True, 35]))

''' MITASK-M
Savol: Shunday function yozing, u string qabul qilsin va string palindrom yani togri oqilganda ham, 
orqasidan oqilganda ham bir hil oqiladigan soz ekanligini aniqlab boolean qiymat qaytarsin.
MASALAN: palindrom_check("dad") return True;  palindrom_check("son") return False;

# Masalaning yechimi:


def palindrom_check(text):
    return text == text[::-1]


print(palindrom_check("son"))
'''
'''
MITASK-K
Savol: Shunday function yozing, u string qabul qilsin va string ichidagi eng uzun sozni qaytarsin.
MASALAN: find_longest("I come from Uzbekistan") return "Uzbekistan"

# Masalaning yechimi:


def find_longest(text):
    words = text.split()
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


print(find_longest("I come from Uzbekistan"))
'''

'''
MITASK-I
Savol: Shunday function tuzing, unga string argument pass bolsin. Function ushbu agrumentdagi digitlarni yangi stringda return qilsin
MASALAN: get_digits("m14i1t") return qiladi "141"

# Masalaning yechimi:


def get_digits(text):
    new_text = []
    for ele in text:
        if ele.isdigit():
            new_text.append(ele)
    return "".join(new_text)


print(get_digits("m14i1t"))
'''

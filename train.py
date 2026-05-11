'''
MITASK-K
Savol: Shunday function yozing, u string qabul qilsin va string ichidagi eng uzun sozni qaytarsin.
MASALAN: find_longest("I come from Uzbekistan") return "Uzbekistan"
'''
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

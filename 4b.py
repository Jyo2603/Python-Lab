#4b. Develop a python program to count all the occurrences of vowels, consonants and digits from the given text using Regular expressions.

import re

st = input("Enter the text: ")
v = re.findall('[aeiouAEIOU]', st)
vowel_count = len(v)
consonant_count = len(re.findall('[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]', st))

print("Vowel occurrences =", vowel_count)
print("Consonant occurrences =", consonant_count)

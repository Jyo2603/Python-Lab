#8a. Develop a python program to read 20 random numbers. Display all the odd numbers from this list which are of length 2 and 4.

nums = map(int, input("Enter 20 random numbers: ").split())
oddNums = [num for num in nums if num % 2 != 0]
len2And4 = [num for num in oddNums if len(str(num)) in [2, 4]]
print(len2And4)

# OR

import random

random_numbers = [random.randint(1, 100) for _ in range(20)]

filtered_numbers = [num for num in random_numbers if num % 2 != 0 and len(str(num)) in [2, 4]]

print("Generated Random Numbers:", random_numbers)
print("Odd Numbers of Length 2 and 4:", filtered_numbers)

#3b. Write a python program to perform the following operations using user defined functions
#• Display the maximum and minimum number from the array.
#Display the second largest number from the array without

def find_max_min_second(arr):
    if len(arr) < 2:
        return None, None, None

    max_num = min_num = arr[0]
    second_largest = float('-inf')

    for num in arr[1:]:
        if num > max_num:
            second_largest = max_num
            max_num = num
        elif num < min_num:
            min_num = num
        elif num > second_largest and num < max_num:
            second_largest = num

    return max_num, min_num, second_largest if second_largest != float('-inf') else None

arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
max_num, min_num, second_largest = find_max_min_second(arr)

print("Maximum number:", max_num)
print("Minimum number:", min_num)
print("Second largest number:", second_largest)

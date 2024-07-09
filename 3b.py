#3b. Write a python program to perform the following operations using user defined functions
#• Display the maximum and minimum number from the
array.
#Display the second largest number from the array without

def find_max_min(arr):
    max_num = min_num = arr[0]
    for num in arr[1:]:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    return max_num, min_num

def find_second_largest(arr):
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second if second != float('-inf') else None

arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
max_num, min_num = find_max_min(arr)
second_largest = find_second_largest(arr)

print("Maximum number:", max_num)
print("Minimum number:", min_num)
print("Second largest number:", second_largest)

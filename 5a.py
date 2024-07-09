#5a. Write a python program to create a tuple and perform the following operations
#• Adding an items
#• Displaying the length of the tuple
#• Checking for an item in the tuple
#Accessing an item

def add_item(tpl, item):
    return tpl + (item,)

def display_length(tpl):
    return len(tpl)

def check_item(tpl, item):
    return item in tpl

def access_item(tpl, index):
    return tpl[index]

tpl = tuple(map(int, input("Enter numbers separated by spaces: ").split()))
tpl = add_item(tpl, int(input("Enter an item to add to the tuple: ")))
print("Tuple:", tpl)
print("Length of the tuple:", display_length(tpl))
print("Is the item present in the tuple?", check_item(tpl, int(input("Enter an item to check: "))))
index = int(input("Enter the index of the item to access: "))
print("Item at index", index, ":", access_item(tpl, index) if 0 <= index < len(tpl) else "Index out of range")

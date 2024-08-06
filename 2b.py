#2b. Write a python program to create a list with all the subject names of the
#4th semester and perform the following operations.
#• Display the list using for loop.
#• Display 2nd and 5th element of the list.
#• Display first 4 elements of the list using the range of indexes.
#• Display last 4 elements of the list using the range of negative indexes.
#• Display if "Python Programming Lab" is available in the List or not.
#• Demonstrate the working of append () and insert () function.
#Demonstrate the working of remove() and pop() function.

def main():
    n = input("enter no. of subjects:")
    subjects=input("enter subjects: ").split()
    
    print("\nAll subjects:")
    for s in subjects:
        print(s)

    if len(subjects) > 4:
        print("\n2nd and 5th subjects:", subjects[1], subjects[4])
    if len(subjects) > 3:
        print("\nFirst 4 subjects:", subjects[:4])
        print("\nLast 4 subjects:", subjects[-4:])
    
    print("\nPython Programming Lab is", "available" if "Python Programming Lab" in subjects else "not available")

    subjects.append("New Subject")
    print("\nAfter appending:", subjects)
    
    subjects.insert(2, "Inserted Subject")
    print("\nAfter inserting at 3rd position:", subjects)
    
    subjects.remove("New Subject")
    print("\nAfter removing:", subjects)
    
    if len(subjects) > 2:
        subjects.pop(2)
        print("\nAfter popping 3rd position:", subjects)

if __name__ == "__main__":
    main()

#7b. Write a python program to utilize NumPy and perform the following operations.
#• Read and display a 2D Array.
#• Display the array elements in the reverse order.
#• Display all the elements of principal diagonal elements.
#• Sort the 2D array in ascending and descending order

import numpy as np

def main():
    array = np.array([list(map(int, input("Enter row elements separated by spaces: ").split())) for _ in range(int(input("Enter number of rows: ")))])
    
    print("Original Array:\n", array)
    print("Array in Reverse Order:\n", array[::-1, ::-1])
    print("Principal Diagonal Elements:", np.diag(array))
    
    flat_array = array.flatten()
    print("2D Array in Ascending Order:\n", np.sort(flat_array).reshape(array.shape))
    print("2D Array in Descending Order:\n", np.sort(flat_array)[::-1].reshape(array.shape))

if __name__ == "__main__":
    main()

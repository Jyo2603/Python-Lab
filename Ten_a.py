#10a. Develop a python program to demonstrate handling of following exceptions using try and except. 
# NameError 
# IndexError 
# KeyError 
# ZeroDivisionError 

def handle_exceptions():
    try:
        operation = int(input("Choose an operation (1 for NameError, 2 for IndexError, 3 for KeyError, 4 for ZeroDivisionError): "))

        if operation == 1:
            print(unknown_variable) 

        elif operation == 2:
            lst_size = int(input("Enter the number of elements in the list: "))
            lst = [int(input("Enter element {}: ".format(i + 1))) for i in range(lst_size)]
            index = int(input("Enter an index to access in the list: "))
            print(lst[index]) 
            
        elif operation == 3:
            d_size = int(input("Enter the number of key-value pairs in the dictionary: "))
            d = {}
            for i in range(d_size):
                key = input("Enter key {}: ".format(i + 1))
                value = int(input("Enter value for key '{}': ".format(key)))
                d[key] = value
            key = input("Enter a key to access in the dictionary: ")
            print(d[key]) 

        elif operation == 4:
            num1 = int(input("Enter the numerator: "))
            num2 = int(input("Enter the denominator: "))
            result = num1 / num2 
            print("The result is:", result)

        else:
            print("Invalid selection")

    except NameError:
        print("NameError caught: The variable used is not defined.")
    except IndexError:
        print("IndexError caught: The index is out of range.")
    except KeyError:
        print("KeyError caught: The key does not exist in the dictionary.")
    except ZeroDivisionError:
        print("ZeroDivisionError caught: Cannot divide by zero.")
    except Exception as e:
        print("An unexpected error occurred: " + str(e))
    finally:
        print("Execution of the try-except-finally block is complete.")

handle_exceptions()

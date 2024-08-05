#9b. Develop a python program to demonstrate handling multipleexceptions using try, except , else and finally block statements.

def divide_numbers():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = num1 / num2
        
        my_dict = {'a': 1, 'b': 2, 'c': 3}
        key = input("Enter a key to access in the dictionary: ")
        value = my_dict[key]
        
    except ValueError:
        print("ValueError caught: Please enter valid integers.")
    except ZeroDivisionError:
        print("ZeroDivisionError caught: Cannot divide by zero.")
    except KeyError:
        print("KeyError caught: The key does not exist in the dictionary.")
    except Exception as e:
        print("An unexpected error occurred: " + str(e))
    else:
        print("The result of dividing {} by {} is {}.".format(num1, num2, result))
        print("The value for the key '{}' is {}.".format(key, value))
    finally:
        print("Execution of the try-except-finally block is complete.")

# Call the function to demonstrate exception handling
divide_numbers()

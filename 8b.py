#8b. Develop a python program to create a text file and ask the user to enter 5-6 lines of text. Count the number of upper case, lower case and digits in the file. Display the details of the file.

def count_chars(text):
    upper_count = sum(1 for char in text if char.isupper())
    lower_count = sum(1 for char in text if char.islower())
    digit_count = sum(1 for char in text if char.isdigit())
    return upper_count, lower_count, digit_count

def main():
    lines = []
    print("Enter 5-6 lines of text:")
    for _ in range(5):
        lines.append(input())
    
    with open("text_file.txt", "w") as file:
        file.write("\n".join(lines))
    
    with open("text_file.txt", "r") as file:
        content = file.read()
        upper_count, lower_count, digit_count = count_chars(content)
        
        print("Content of the File:")
        print(content)
        print("Number of Uppercase Letters:", upper_count)
        print("Number of Lowercase Letters:", lower_count)
        print("Number of Digits:", digit_count)

if __name__ == "__main__":
    main()

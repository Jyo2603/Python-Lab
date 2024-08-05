#8b. Develop a python program to create a text file and ask the user to enter 5-6 lines of text. Count the number of upper case, lower case and digits in the file. Display the details of the file.

def count_chars(text):
    return (sum(c.isupper() for c in text),
            sum(c.islower() for c in text),
            sum(c.isdigit() for c in text))

def main():
    lines = [input() for _ in range(5)]
    
    with open("text_file.txt", "w") as file:
        file.write("\n".join(lines))
    
    with open("text_file.txt", "r") as file:
        content = file.read()
        upper, lower, digits = count_chars(content)
        print("\nFile Content:\n", content)
        print("Uppercase Letters:", upper)
        print("Lowercase Letters:", lower)
        print("Digits:", digits)

if __name__ == "__main__":
    main()

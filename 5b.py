#5b. Write a python program to create a text file and ask the user to enter 5-6 lines of text. Display the longest and the shortest word from the file. Display the length of these words.

def get_longest_and_shortest(words):
    longest_word = max(words, key=len)
    shortest_word = min(words, key=len)
    return longest_word, shortest_word

file_name = 'text_file.txt'
with open(file_name, 'w') as file:
    for i in range(5):
        line = input(f"Enter line {i+1}: ") + '\n'
        file.write(line)

with open(file_name, 'r') as file:
    content = file.read()

words = content.split()

longest_word, shortest_word = get_longest_and_shortest(words)

print("\nLongest word:", longest_word)
print("Length of longest word:", len(longest_word))
print("\nShortest word:", shortest_word)
print("Length of shortest word:", len(shortest_word))

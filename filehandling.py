# Create and write data into student.txt
file = open("student.txt", "w")
file.write("Name: Rujuta Patil\n")
file.write("Roll Number: 21\n")
file.write("Branch: Computer Science and Engineering\n")
file.write("Semester: 5\n")
file.close()
print("Student details written successfully.")

# Open the file in read mode
file = open("student.txt", "r")
content = file.read()
print(content)
file.close()

# Open the file in append mode
file = open("student.txt", "a")
file.write("\nName: Rahul Patil")
file.write("\nRoll Number: 22")
file.write("\nBranch: CSE")
file.write("\nSemester: 4")
file.close()
print("Additional student information appended successfully.")

# Open the file in read mode
file = open("student.txt", "r")
for line in file:
    print(line.strip())
file.close()

# Open the file in read mode
file = open("student.txt", "r")
count = 0
for line in file:
    count += 1
print("Total number of lines:", count)
file.close()

# Open the file in read mode
file = open("student.txt", "r")
# Read the complete contents of the file
data = file.read()
# Split the contents into words
words = data.split()
# Count and display the total number of words
print("Total number of words:", len(words))
# Close the file
file.close()

# Open the file in read mode
file = open("student.txt", "r")
# Read the complete contents of the file
data = file.read()
# Count the total number of characters
count = len(data)
# Display the total number of characters
print("Total number of characters:", count)
# Close the file
file.close()

# Open the file in read mode
file = open("student.txt", "r")
# Read all lines from the file
lines = file.readlines()
# Display the lines in reverse order
for line in reversed(lines):
    print(line.strip())
# Close the file
file.close()

# Open the file in read mode
file = open("student.txt", "r")
# Read the complete contents of the file
data = file.read()
# Initialize counters
vowels = 0
consonants = 0
# Check each character
for ch in data:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
# Display the results
print("Total number of vowels:", vowels)
print("Total number of consonants:", consonants)
# Close the file
file.close()

# Open the file in read mode
file = open("student.txt", "r")
# Read the complete contents of the file
data = file.read()
# Initialize counters
alphabets = 0
digits = 0
spaces = 0
special = 0
# Check each character
for ch in data:
    if ch.isalpha():
        alphabets += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    elif ch != "\n":
        special += 1
# Display the results
print("Total alphabets:", alphabets)
print("Total digits:", digits)
print("Total spaces:", spaces)
print("Total special characters:", special)
# Close the file
file.close()

# Open the file in read mode
file = open("student.txt", "r")
# Read the complete contents of the file
data = file.read()
# Split the contents into words
words = data.split()
# Find the longest word
longest_word = max(words, key=len)
# Display the longest word
print("Longest word:", longest_word)
# Close the file
file.close()

# Open the file in read mode
file = open("student.txt", "r")
# Read the complete contents of the file
data = file.read()
# Split the contents into words
words = data.split()
# Create an empty dictionary
word_count = {}
# Count each word
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
# Display the result
print("Word Frequency:")
print(word_count)
# Close the file
file.close()
# Open the file in read mode
file = open("student.txt", "r")
# Accept a word from the user
search_word = input("Enter the word to search: ")
# Initialize variables
count = 0
line_numbers = []
# Read the file line by line
for line_number, line in enumerate(file, start=1):
    words = line.split()
    # Check each word in the line
    for word in words:
        if word.lower() == search_word.lower():
            count += 1
            # Store the line number
            if line_number not in line_numbers:
                line_numbers.append(line_number)
# Display the result
if count > 0:
    print("Number of occurrences:", count)
    print("Word found on line(s):", line_numbers)
else:
    print("Word not found in the file.")
# Close the file
file.close()
# Open the file in read mode
file = open("student.txt", "r")
# Read the complete contents of the file
data = file.read()
# Accept words from the user
old_word = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")
# Replace the old word with the new word
modified_data = data.replace(old_word, new_word)
# Open the same file in write mode
file = open("student.txt", "w")



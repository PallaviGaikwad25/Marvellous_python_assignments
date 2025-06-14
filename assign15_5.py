import string

filename = input("Enter the file name: ")
search_word = input("Enter the word to search: ").strip().lower()

count = 0

with open(filename, "r") as file:
    for line in file:
        words = line.split()
        for word in words:
            
            clean_word = word.strip(string.punctuation).lower()# Remove punctuation and make lowercase
            if clean_word == search_word:
                count += 1

print("The word count is=",clean_word)


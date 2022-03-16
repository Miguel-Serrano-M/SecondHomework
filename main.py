#Second Homework

#1 question

from urllib.request import urlopen

local_name = "text.txt"

import certifi
import ssl


url = ()
Book1 = "https://www.gutenberg.org/files/67632/67632-0.txt"
Book2= "https://www.gutenberg.org/files/67635/67635-0.txt"

urls = input("Do you want to count first Book 1 or Book 2?:")
if urls == "Book 1":
    url = Book1
elif urls == "Book 2":
    url = Book2


def save_locally():

    with open(local_name, "w") as local_fp:
        with urlopen(url, context=ssl.create_default_context(cafile=certifi.where())) as fp:
            for line in fp:
                line = line.decode('utf-8-sig').replace("\n", "")
                local_fp.write(line)


punctuation = ",;!.?-()"
def get_unique_words():

    unique_words = {}
    with open(local_name) as fp:
        for line in fp:
            for p in punctuation:
                line = line.replace(p, " ")
            line = line.lower()
            for word in line.split():
                unique_words[word] = unique_words.get(word, 0) + 1

    return unique_words


save_locally()
unique_words = get_unique_words()
most_frequent = list(unique_words.values())
most_frequent.sort(reverse=True)
for word_frequency in most_frequent[0:]:
    for unique_word, value in unique_words.items():
        if word_frequency == value:
            print(f"common word '{unique_word}' appears {value} times")
            unique_words[unique_word] = -1
            break


a =len(unique_words)
print(a)


#When running one book first and the the other one after we can see how Book 2 has a much wider vocabulary of words

#2 Question
seven = []


for word in url:
    if len(word) >=7:
        seven.append(word)

print(seven)

#I am not able to make this excercise

#3 question

file = open("text.txt", "r")
words = file.read()
count_words = words.split()

print("Total words", len(count_words))

# The 2nd book has more words in distinct words and in total number of words
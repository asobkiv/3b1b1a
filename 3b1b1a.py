# HONOR PLEDGE
# I, (Name, Surname), fully aknowledge the consequences of
# academic misconduct.
# During my work, I:
# 1. Received help from: ChatGPT(line 44-57)
# 2. Consulted following materials: w3schools.com, geeksforgeeks.org, stackoverflow.com
""" Choose a book that you like (Keep it under 3mb)
1. Download the book in .txt format
2. Create a python file. In it:
1. Open the book file
2. (optional) Clean the text file, e. g. lowercase
everything etc.
3. split the text into a list of its tokens (i. e.
words and punctuation). You may use native python
methods or consult other libraries
4. Create a dictionary object, where:
1. the keys are the unique tokens
2. the values are lists of the next following
words that occur after the key token (1 next
word for every occurrence)
5. Generate text. Make it so that:
1. the program chooses the first word randomly
from the keys and prints it (you can use  random
library for this)
2. then it consults the occurrence list from the
dictionary you created to randomly choose the
next word to print out (you can use  random
library for this)
"""
import re
import random
favourite_book = open("1984.txt","r").read().lower()
#tokenisation
tokens = re.findall(r'\w+|[^\w\s]',favourite_book)
token_dict = {}
for i in range(len(tokens) - 1):
    current_token = tokens[i]
    next_token = tokens[i + 1]
    if current_token in token_dict:
        token_dict[current_token].append(next_token)
    else:
        token_dict[current_token] = [next_token]
#how many words will be picked
num_words = 50
current_token = random.choice(list(token_dict.keys()))
text = [current_token]
for num in range(num_words - 1):
    if current_token in token_dict:
        next_words = token_dict[current_token]
        next_token = random.choice(next_words)
        text.append(next_token)
        current_token = next_token
    else:
        current_token = random.choice(list(token_dict.keys()))
        text.append(current_token)
generated_text = ' '.join(text)
print(generated_text)




#! /usr/bin/env python3

import sys  # command line arguments
import re  # regular expression tools

# set input and output files
if len(sys.argv) is not 3:
    print("Correct usage: wordCount.py <input text file> <output file>")
    exit()

input = sys.argv[1]
output = sys.argv[2]


def regex(key, text_string):
    result = re.findall(r'\b'+key+'\\b', text_string)
    for word in result:
            count = frequency.get(key, 0)
            frequency[word] = count + 1
    return frequency.keys()


# Cleaning key without numbers
clean_key_string = ''
# output
document_key = open('speechKey.txt')
document_key_string = document_key.read()
i = 0
for word in document_key_string:
    clean_key_string += re.sub('[0-9]', '', word)

# Storing words in array
split_key = clean_key_string.split()

frequency = {}
document_text = open(input, 'r')
text_string = document_text.read().lower()
match_pattern_list = []

index = 0
for i in split_key:
        match_pattern_list.append(regex(split_key[index], text_string))
        index += 1

idx = 0
for words in match_pattern_list[1]:
    # output.txt
    file = open(output, 'a')
    file.write(words + " " + str(frequency[words]) + "\n")
    idx += 1
    if idx == len(match_pattern_list[1]):
        print("Number of words found in output.txt")
        file.close()
        exit()




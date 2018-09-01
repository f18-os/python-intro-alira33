#! /usr/bin/env python3

# import sys  # command line arguments
import re  # regular expression tools
# import os  # checking if file exists
# import subprocess  # executing program

# # set input and output files
# if len(sys.argv) is not 4:
#     print("Correct usage: wordCount.py <input text file> <output file>")
#     exit()
#
# textFname = sys.argv[1]
# outputFname = sys.argv[2]
#
# # first check to make sure program exists
# if not os.path.exists("wordCount.py"):
#     print("wordCount.py doesn't exist! Exiting")
#     exit()
#
# # make sure text files exist
# if not os.path.exists(textFname):
#     print("text file input %s doesn't exist! Exiting" % textFname)
#     exit()
#
# # execute the program with
# subprocess.call(["python", "./wordCount.py", textFname, outputFname])
#
# # make sure output file exists
# if not os.path.exists(outputFname):
#     print("wordCount output file %s doesn't exist! Exiting" % outputFname)
#     exit()

# Cleaning key without numbers
clean_key_string = ''
document_key = open('output.txt')
document_key_string = document_key.read()
i = 0
for word in document_key_string:
    clean_key_string += re.sub('[0-9]', '', word)

# Storing words in array
split_key = clean_key_string.split()
print(split_key)



# frequency = {}
# document_text = open('input.txt', 'r')
# text_string = document_text.read().lower()
# match_pattern = re.findall(r'\b[a]{1,2}\b', text_string)
#
# for word in match_pattern:
#     count = frequency.get(word, 0)
#     frequency[word] = count + 1
#
# frequency_list = frequency.keys()
#
# for words in frequency_list:
#     print(words, frequency[words])
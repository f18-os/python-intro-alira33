import sys  # command line arguments
import re  # regular expression tools
import os  # checking if file exists
import subprocess  # executing program

# # set input and output files
# if len(sys.argv) is not 2:
#     print("Correct usage: wordCount.py <input text file> <output file>")
#     exit()
#
# textFname = sys.argv[1]
# outputFname = sys.argv[2]
#
# print(textFname)
# print(outputFname)
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

def count_chars(txt):
        result = 0
        for char in txt:
            result += 1
        return result

def regex(key, text_string):
    result = re.findall(r'\b'+key+'\\b', text_string)
    for word in result:
            count = frequency.get(key, 0)
            frequency[word] = count + 1
    return frequency.keys()


# Cleaning key without numbers
clean_key_string = ''
document_key = open('output.txt')
document_key_string = document_key.read()
i = 0
for word in document_key_string:
    clean_key_string += re.sub('[0-9]', '', word)

# Storing words in array
split_key = clean_key_string.split()

frequency = {}
document_text = open("input.txt", 'r')
text_string = document_text.read().lower()
match_pattern_list = []

index = 0
for i in split_key:
        match_pattern_list.append(regex(split_key[index], text_string))
        index += 1

for words in match_pattern_list[1]:
    file = open("word_match", "a")
    file.write(words + " " + str(frequency[words]) + "\n")
    print(words, frequency[words])




import re

frequency = {}
document_text = open('input.txt', 'r')
text_string = document_text.read().lower()
a = 'accomplished'
match_pattern = re.findall(r'\b'+a+'\\b', text_string)
print(match_pattern)

for word in match_pattern:
    count = frequency.get(word, 0)
    frequency[word] = count + 1

frequency_list = frequency.keys()

for words in frequency_list:
    print(words, frequency[words])

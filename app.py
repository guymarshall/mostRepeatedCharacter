from pprint import pprint

filename = input("Enter a filename to scan: ")
file = open(filename, "r")
sentence = file.read()

char_frequency = {}

for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

pprint(char_frequency, width=1)

char_frequency_sorted = sorted(char_frequency.items(),
                               key=lambda kv: kv[1],
                               reverse=True)
print(char_frequency_sorted[0])

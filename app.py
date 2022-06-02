from pprint import pprint

file_name = input("Enter a filename to scan: ")
file = open(file_name, "r")
file_contents = file.read()

character_frequency = {}

for character in file_contents:
    if character in character_frequency:
        character_frequency[character] += 1
    else:
        character_frequency[character] = 1

pprint(character_frequency, width=1)

character_frequency_sorted = sorted(character_frequency.items(), key=lambda kv: kv[1], reverse=True)

print(character_frequency_sorted[0])

text = "programming"
char_count = {}

for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)

word="aabbc"
char_count={}
for char in word:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
compressed_string = ""
for char, count in char_count.items():
    compressed_string += f"{char}{count}"

print("Original:", word)
print("Compressed:", compressed_string)
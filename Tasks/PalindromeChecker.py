words = ["radar", "hello", "level", "python", "madam"]

for w in words:
    reversed_word = w[::-1]
    if w == reversed_word:
        print(f"{w} is a Palindrome")
    else:
        print(f"{w} is NOT a Palindrome")
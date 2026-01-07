text = "python is great python is fun"
word_count={}
for word in text.split():
    word_count[word]=word_count.get(word,0)+1
print(word_count)
    #it is also done by if-else statement 

text="I love apples"
old_word="apples"
new_word="mangoes"
words=text.split()
for i in range(len(words)):
    if words[i]==old_word:
        words[i]=new_word
final_text=" ".join(words)
print("original",text)
print("final",final_text)

text = "Python 3.10 is Great!"
up_count=0
low_count=0
digital_count=0
space_count=0
for i in text:
    if i.isupper():
        up_count+=1
    elif i.islower():
        low_count+=1
    elif i.isdigit():
        digital_count+=1
    elif i==" ":
        space_count+=1
print("Upper case letters:", up_count)
print("Lower case letters:", low_count)
print("Digits:", digital_count)
print("Spaces:", space_count)
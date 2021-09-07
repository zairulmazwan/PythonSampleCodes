
text = "I like programming. I study programming at Sheffield Hallam University. My favourite programming language is Python";

print("This is a text")
print(text)

print("\nI want to convert the text into a list variable")
textList = text.split()
print(textList)

print("\nBut some of the words have special character, how do i remove them?")
import re
cleanedWords=[]
for i in textList:
    cleanedWords += [re.sub(r"[^a-zA-Z0-9]","",i)]
print(cleanedWords)

print("\nHow do I get a set of distinct words from the text?")
distinct = set(cleanedWords)
print(distinct)

print("\nI want to create an empty dictionary")
dict = {}
print(dict)

print("\nHow I make the distinct words as the key in the dictionary variable and default the value to 0?")
dict = {word : 0 for word in distinct}
print(dict)

print("\nHow do i count the words and update the dictionary?")
# for word in dict:
#     for i in cleanedWords:
#         if i==word:
#             dict[word]+=1

#or you can simplify this way
for word in dict:
    count = cleanedWords.count(word)
    dict[word]=count

print(dict)


methods = dir("hi")
useful_methods = []
for method in methods:
    if "__" in method:
        continue
    useful_methods.append(method)
print(useful_methods)

print(help("hi".capitalize)) # get help for whatever method you want
print("cat".capitalize())
s = "i go to uni every day."
print(s.capitalize())

print(help("".casefold))
print("I LIKE CAKE".casefold()) # lower pretty much does the same thing

print("hello".center(30, "*"))
print("bananananaanananananan".count("ana")) # count is useful!

print("ana ana banana".find("ana")) # 0 because the first "ana" is at position 0

print("abcdebg".index("b", 2))

words = ["i", "like", "to", "sing"]
print(" ".join(words))

s = "I like to go hiking!"
print(s.replace(" ", "! !"))

s = "I like to go hiking!"
#print(s.split())
print(s.replace("!", "").split())
print(s.upper())
punctuation = "!,?-;/'"
sentence = "How, are, you? I don't like this;"
for p in punctuation:
    sentence = sentence.replace(p, "")
print(sentence)

print("i like to go skiing".title())

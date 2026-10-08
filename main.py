fhand = open('romeo.txt')

words = []

for line in fhand:
    every_words = line.split()
    for word in every_words:
        if word not in words:
            words.append(word)

words.sort()
print(words)
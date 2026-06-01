import string


with open("test.txt", "r") as f:
    text = f.read()
    text = text.translate(str.maketrans("", "", string.punctuation))
# print(text)

words = text.lower().split()
print(words)

counts = {}

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

# print(counts)
top = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:10]
print(top)

for word, count in top:
    print(word, count)

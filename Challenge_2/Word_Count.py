#PART 4: WORD COUNT FOR LISTS

string = 'hi dee hi how are you mr dee'
word_count = {}
words = string.split()

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

for word, count in word_count.items():
    print(f"{word}: {count}")


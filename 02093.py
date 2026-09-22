#text = "привет как настроение"
text = input()
#words = text.split()

#num_longest_word = 0
#for word in words:
#    if len(word) > 5:
#        num_longest_word += 1
#print(num_longest_word)

#print(len([word for word in text.split() if len(word) > 5]))
words = text.split()
long_words = [word for word in text.split() if len(word) > 5]
print(len(long_words))

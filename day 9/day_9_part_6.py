text = """“Любіть Україну, як сонце, любіть,

як вітер, і трави, і води…

В годину щасливу і в радості мить,

любіть у годину негоди.

Любіть Україну у сні й наяву,

вишневу свою Україну,

красу її, вічно живу і нову,

і мову її солов’їну.

Між братніх народів, мов садом рясним,

сіяє вона над віками…

Любіть Україну всім серцем своїм

і всіми своїми ділами.

Для нас вона в світі єдина, одна

в просторів солодкому чарі…

Вона у зірках, і у вербах вона,

і в кожному серця ударі,

у квітці, в пташині, в електровогнях,

у пісні у кожній, у думі,

в дитячий усмішці, в дівочих очах

і в стягів багряному шумі…”"""

text = text.lower()

punctuation = '…“,.”'

text_without_punct = ''

for char in text:
    if char not in punctuation:
        text_without_punct += char

words = text_without_punct.split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)

max_word = max(word_count, key=word_count.get)

print(f"Maximum, the word '{max_word}' was {word_count[max_word]} times in the text")
print("Minimum, the words below were once in the text:")

keys_with_count_1 = []
for key, value in word_count.items():
  if value == 1:
    keys_with_count_1.append(key)
    print(key)







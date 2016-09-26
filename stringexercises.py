#prints the sentence in uppercase
sentence = raw_input("Please give me a sentence. ")
print sentence.upper()

#capitalizes the sentence
sentence = raw_input("Please give me a sentence. ")
print sentence.capitalize()

#reverses the sentence
sentence = raw_input("Please give me a sentence. ")
# print sentence[::-1]
empty = ""
for i in sentence:
     i + empty
     print empty


#ciphers the users sentence
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
 "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
shiftedAlphabet = ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
 "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", " "]
sentence = raw_input("put in a sentence ")
cipher = ''

for letter in sentence:
    position = alphabet.index(letter)
    shiftedletter = shiftedAlphabet[position]
    cipher = cipher + shiftedletter
print cipher


#decipher
shiftedAlphabet = ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
 "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", " "]
Alphabet = ["a" "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
 "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

decipher = ''

for letter in sentence:
    position = shiftedAlphabet.index(letter)
    shiftbackletter = shiftedAlphabet[position]
    decipher = decipher + shiftbackletter
print decipher

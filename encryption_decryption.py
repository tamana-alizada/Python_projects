# It is taken from BroCode YouTube Channel, Python Full Course For Free
import random
import string

chars = " " + string.punctuation + string.ascii_letters + string.digits
chars = list(chars)
key = chars.copy()
random.shuffle(key)

print(chars)
print(key)

# Encryption
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
  index = chars.index(letter)
  cipher_text += key[index]
print(cipher_text)

# Decryption
cipher_text = input("Enter a message to decrypt: ")
plain_text = ""
for letter in cipher_text:
  index = key.index(letter)
  plain_text += chars[index]

print(plain_text)

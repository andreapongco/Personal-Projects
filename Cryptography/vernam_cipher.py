import string
import random


def generate_key(text):

    text = list(text.split(" "))
    text = "".join(text)

    key = ""
    alphabet = list(string.ascii_uppercase)

    for i in range(0, len(text)):
        key += random.choice(alphabet)

    return key


def vernam_cipher(text, key):
    text = list(text.split(" "))
    text = "".join(text).upper()
    ciphertext = ""
    alphabet = list(string.ascii_uppercase)

    for i in range(0, len(text)):
        index = alphabet.index(text[i]) ^ alphabet.index(key[i].upper())
        if index >= 26:
            index -= 26
        ciphertext += alphabet[index]
    return ciphertext


text = "I have a bread and a sandwich"
key = generate_key(text)
encrypted_text = vernam_cipher(text, key)
print(encrypted_text)
decrypted_text = vernam_cipher(encrypted_text, key)
print(decrypted_text)

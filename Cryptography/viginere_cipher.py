import random
import string


def encrypt_with_vigenere(plaintext, keyword):

    plain_text_arr = plaintext.split(" ")
    plain_text_arr = [x.upper() for x in plain_text_arr]
    alphabet = list(string.ascii_uppercase)

    encrypted_text = ""

    plaintext = "".join(plain_text_arr)

    key = ""

    while len(key) <= len(plaintext):
        key += keyword.upper()

    for i in range(0, len(plaintext)):
        index = (alphabet.index(plaintext[i]) + alphabet.index(key[i])) % 26
        encrypted_text += alphabet[index]

    return encrypted_text


def decrypt_with_vigenere(ciphertext, keyword):

    decypted_text = ""
    alphabet = list(string.ascii_uppercase)

    key = ""

    while len(key) <= len(ciphertext):
        key += keyword.upper()

    for i in range(0, len(ciphertext)):
        index = (alphabet.index(
            ciphertext[i].upper()) - alphabet.index(key[i])) % 26
        decypted_text += alphabet[index]

    return decypted_text


print(encrypt_with_vigenere("We are discovered save yourself", "deceptive"))
print(decrypt_with_vigenere("ZICVTWQNGRZGVTWAVZHCQYGLMGJ", "deceptive"))

import string
import random
print("====== Welcome to Shift Cipher Encryptor ======")

plain_text = str(input("Enter a text to encrypt: "))

alphabet = list(string.ascii_uppercase)
key = random.randint(0, 25)

# encryption


def encrypt_in_shift_cipher(plain_text, alphabet):
    ciphertext = ""
    for i in range(0, len(plain_text)):
        C = (alphabet.index(plain_text[i].upper()) + key) % 26
        ciphertext += alphabet[C]

    return (ciphertext)

# decryption


def shift_cipher_cryptanalysis(ciphertext, alphabet):
    cryptanalysis = {}
    for i in range(1, 26):
        plain_text = ""

        for j in range(0, len(ciphertext)):
            p = (alphabet.index(ciphertext[j]) - i) % 26
            plain_text += alphabet[p]

        cryptanalysis[f"[{i}]"] = plain_text
    return cryptanalysis

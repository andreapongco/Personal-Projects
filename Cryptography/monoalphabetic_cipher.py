import string

alphabet = list(string.ascii_uppercase)


def create_cipher_dictionary(alphabet):
    cipher_dictionary = {}

    for i in range(0, 26):
        key = str(input("Enter letter for " + alphabet[i] + ": ")).upper()

        while key in list(cipher_dictionary.values()) or key == '':
            print(
                f"The key has already been assigned or key is empty. Please try again."
            )
            key = str(input("Enter letter for " + alphabet[i] + ": ")).upper()

        cipher_dictionary[alphabet[i]] = key

    return (cipher_dictionary)


def encrypt_in_monoalphabetic(plain_text, alphabet):

    cipher_text = ""
    cipher_dictionary = create_cipher_dictionary(alphabet)

    # encryption

    for i in plain_text.upper():

        if i == ' ' or i in [
                "!", "\"", "#", "$", "%", "&", "\'", "(", ")", "*", "+", ",",
                "-", ".", "/", ":", ";", "?", "@", "[", "\\", "]", "^", "_",
                "`", "{", "|", "}", "~"
        ]:
            cipher_text += i
        else:
            cipher_text += cipher_dictionary[i]

    return (cipher_text)


def decrypt_in_monoalphabetic(ciphertext, alphabet):

    plain_text = ""
    cipher_dictionary = create_cipher_dictionary(alphabet)

    for i in ciphertext:
        if i == ' ' or i in [
                "!", "\"", "#", "$", "%", "&", "\'", "(", ")", "*", "+", ",",
                "-", ".", "/", ":", ";", "?", "@", "[", "\\", "]", "^", "_",
                "`", "{", "|", "}", "~"
        ]:
            plain_text += i
        else:
            for p, c in cipher_dictionary.items():
                if c == i:
                    plain_text += p

    return (plain_text)


plain_text = str(input("Enter the text to encrypt: "))
encrypted_text = encrypt_in_monoalphabetic(plain_text, alphabet)
print(f"The encrypted text is {encrypted_text}")
decrypted_text = decrypt_in_monoalphabetic(encrypted_text, alphabet)
print(f"The decrypted text is {decrypted_text}")

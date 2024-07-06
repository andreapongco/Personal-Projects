import string
import random


def encrypt_row_column_transposition(text, key, row, col):

    key = [int(x) for x in key]
    text = "".join(text.upper().split(" "))
    matrix = [["" for x in range(0, col)] for x in range(0, row)]
    order_dict = {}
    encrypted_text = ''

    if len(key) != (row * col):
        iter = (row * col) - len(key)

        for i in range(0, iter):
            text += random.choice(string.ascii_uppercase)

    for i in range(0, len(key)):
        order_dict[i] = key[i]

    sorted_dict = sorted(order_dict.items(), key=lambda item: item[1])
    col_order = [x[0] for x in sorted_dict]

    k = 0
    for i in range(0, row):
        for j in range(0, col):
            matrix[i][j] = text[k]
            k += 1

    for c in col_order:
        for r in range(0, row):
            encrypted_text += matrix[r][c]

    return encrypted_text


def decrypt_row_column_transposition(text, key, row, col):
    key = [int(x) for x in key]
    matrix = [["" for x in range(0, col)] for x in range(0, row)]
    order_dict = {}
    decrypted_text = ""

    for i in range(0, len(key)):
        order_dict[i] = key[i]

    sorted_dict = sorted(order_dict.items(), key=lambda item: item[1])
    col_order = [x[0] for x in sorted_dict]

    k = 0
    for c in col_order:
        for r in range(0, row):
            matrix[r][c] = text[k]
            k += 1

    for r in range(0, row):
        for c in range(0, col):
            decrypted_text += matrix[r][c]

    return (decrypted_text)


print(encrypt_row_column_transposition(
    "Kill Corona Virus at twelve am tomorrow", "4312567", 5, 7))
print(decrypt_row_column_transposition(
    "LATARLVTMOINAERKOSVOCIWTWOREOARULMO", "4312567", 5, 7))

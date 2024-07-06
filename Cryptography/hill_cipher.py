import numpy as np
import string
import random
from sympy import mod_inverse
import sympy as sp


def encrypt_in_hill(text, key):

    key = np.array(key)
    const = 3
    text = "".join(text.upper().split(" "))
    alphabet = list(string.ascii_uppercase)
    num_arr = []
    result = ""

    if len(text) % const > 0:
        while len(text) % const > 0:
            text += random.choice(alphabet)

    for i in text:
        num_arr.append(alphabet.index(i))

    num_arr = [np.array(num_arr[i:i+const])
               for i in range(0, len(num_arr), const)]

    for i in num_arr:
        for j in range(0, const):
            result += alphabet[(i @ key[:, j]) % 26]

    return (result)


def decrypt_in_hill(text, key):
    key = np.array(key)
    const = 3
    result = ""
    determinant = np.linalg.det(key) % 26
    adjoint = sp.Matrix(key).adjugate() % 26
    adjoint = np.array([np.array(adjoint[i:i+const])
                        for i in range(0, len(adjoint[0:]), const)])
    inverse = (mod_inverse(int(determinant), 26) * adjoint) % 26
    alphabet = list(string.ascii_uppercase)
    num_arr = []

    for i in text:
        num_arr.append(alphabet.index(i))

    num_arr = [np.array(num_arr[i:i+const]) for i in range(0, len(num_arr), 3)]

    for i in num_arr:
        for j in range(0, const):
            result += alphabet[(i @ inverse[:, j]) % 26]

    return (result)


encrpyted_text = encrypt_in_hill(
    "pay more money", [[17, 17, 5], [21, 18, 21], [2, 2, 19]])
print(encrpyted_text)
decrypted_text = decrypt_in_hill(
    encrpyted_text, [[17, 17, 5], [21, 18, 21], [2, 2, 19]])
print(decrypted_text)

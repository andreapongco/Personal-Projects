import string


def create_matrix(keyword):
    diagram = []
    final_diagram = []
    alphabet = string.ascii_uppercase
    keyword = keyword.replace(" ", "")

    for i in keyword.upper():
        if i not in diagram:
            diagram.append(i)

    for i in alphabet:
        if i not in diagram and i != "J":
            diagram.append(i)

    for i in range(0, len(diagram), 5):
        final_diagram.append(diagram[i:i+5])

    return final_diagram


def partition_text(plain_text):

    plain_text = plain_text.upper()
    plain_text = plain_text.replace(" ", "")
    partitioned_text = []

    for i in range(0, len(plain_text), 2):
        data = plain_text[i:i+2]
        if len(data) != 2:
            data += "X"
        partitioned_text.append(data)

    return (partitioned_text)


def check_same_column(matrix, pair):

    coordinates = []
    result = ""

    for l in pair:
        for c in range(0, 5):
            for r in range(0, 5):
                if matrix[r][c] == l:
                    if r < 4:
                        result += matrix[r+1][c]
                    else:
                        result += matrix[0][c]
                    coordinates.append(c)

    if coordinates[0] == coordinates[1]:
        return result
    else:
        return ""


def check_same_row(matrix, pair):
    coordinates = []
    result = ""

    for l in pair:
        for r in range(0, 5):
            for c in range(0, 5):
                if matrix[r][c] == l:
                    if c < 4:
                        result += matrix[r][c+1]
                    else:
                        result += matrix[r][0]
                    coordinates.append(r)
    if coordinates[0] == coordinates[1]:
        return result
    else:
        return ""


def rectangle(matrix, pair):

    coordinates = []
    result = ""

    for l in pair:
        for r in range(0, 5):
            for c in range(0, 5):
                if matrix[r][c] == l:
                    coordinates.append([r, c])
    # first letter is same row but the column of second coordinate

    result = matrix[coordinates[0][0]][coordinates[1][1]] + \
        matrix[coordinates[1][0]][coordinates[0][1]]
    return result


def encrypt_in_playfair_cipher(plain_text, keyword):

    diagram = create_matrix(keyword=keyword)
    partitioned_text = partition_text(plain_text=plain_text)
    cipher_dict = {}
    i = 0

    while i < len(partitioned_text):

        result = check_same_column(diagram, partitioned_text[i])
        if result != "":
            cipher_dict[partitioned_text[i]] = result
            i += 1
        else:
            result = check_same_row(diagram, partitioned_text[i])
            if result != "":
                cipher_dict[partitioned_text[i]] = result
                i += 1
            else:
                cipher_dict[partitioned_text[i]] = rectangle(
                    diagram, partitioned_text[i])
                i += 1

    return "".join(list(cipher_dict.values()))


plain_text = str(input("Enter the text to encrypt: "))
keyword = str(input("Enter the keyword to be used: "))

print(encrypt_in_playfair_cipher(plain_text=plain_text, keyword=keyword))

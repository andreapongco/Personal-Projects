def encrypt_rail_fence(text, depth):

    text = "".join(text.upper().split(" "))

    ciphertext = ""
    rail_fence = []

    # set-up the rail fence
    for i in range(0, depth):
        rail_fence.append(['' for x in range(0, len(text))])

    r = 0
    c = 0
    direction = -1

    # do the fencing
    for i in range(0, len(text)):
        rail_fence[r][c] = text[i]
        c += 1
        if r == 0:
            direction = 1
        elif r == (depth-1):
            direction = -1
        r += direction

    for i in rail_fence:
        ciphertext += "".join(i)

    return ciphertext


def decrypt_rail_fence(text, depth):
    plain_text = ""
    rail_fence = [["" for x in range(0, len(text))] for x in range(0, depth)]

    # fill the rail fence with a zigzag pattern

    r = 0
    c = 0
    direction = -1

    for i in range(0, len(text)):
        rail_fence[r][c] = "*"
        c += 1
        if r == 0:
            direction = 1
        elif r == (depth-1):
            direction = -1
        r += direction

    move_text = 0
    # fill the fence
    for i in range(0, depth):
        for j in range(0, len(text)):
            if rail_fence[i][j] == "*" and move_text < len(text):
                rail_fence[i][j] = text[move_text]
                move_text += 1

    r = 0
    c = 0
    direction = -1
    for i in range(0, len(text)):
        plain_text += rail_fence[r][c]
        if r == 0:
            direction = 1
        elif r >= (depth-1):
            direction = -1
        r += direction
        c += 1
    return (plain_text)


encrypted_text = encrypt_rail_fence("neso academy is the best", 3)
decrypted_text = decrypt_rail_fence(encrypted_text, 3)
print(encrypted_text)
print(decrypted_text)

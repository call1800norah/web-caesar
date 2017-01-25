def alphabet_position(letter):
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'

    for ch in upper:
         if ch == letter:
            return upper.find(letter)

    for ch in lower:
         if ch == letter:
            return lower.find(letter)


def rotate_character(char,rot):
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'

    x = alphabet_position(char)
    y = (x + rot) % 26
    z = upper[y]
    zz = lower[y]
    if char in upper:
        return z
    else:
        return zz


def encrypt(text,rot):
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = []
    for char in text:
        if char in upper:
            encrypted.append(rotate_character(char,rot))
        elif char in lower:
            encrypted.append(rotate_character(char,rot))
        else:
            encrypted.append(char)
    encrypted = ''.join(encrypted)
    return encrypted

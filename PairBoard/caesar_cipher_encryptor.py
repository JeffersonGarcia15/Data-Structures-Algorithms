def caesarCipherEncryptor(string, key):
    new_letters = []
    new_key = key % 26
    for letter in string:
        new_letters.append(getNewLetter(letter, new_key))
    return "".join(new_letters)


def getNewLetter(letter, key):
    new_letter_code = ord(letter) + key
    return chr(new_letter_code) if new_letter_code <= 122 else chr(96 + new_letter_code % 122)

# def caesarCipherEncryptor(string, key):
#     new_letters = []
#     new_key = key % 26
#     alphabet = list('abcdefghijklmnopqrstuvwxyz')
#     for letter in string:
#         new_letters.append(getNewLetter(letter, new_key, alphabet))
#     return "".join(new_letters)


# def getNewLetter(letter, key, alphabet):
#     new_letter_code = alphabet.index(letter) + key
#     return alphabet[new_letter_code % 26]


print(caesarCipherEncryptor('xyz', 2))

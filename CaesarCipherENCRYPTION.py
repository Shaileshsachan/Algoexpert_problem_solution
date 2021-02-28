# O(n) time | O(n) space
# def caesarCipherEncryption(string, key):
#     newLetters = []
    # newkey = key % 26
    # for letter in string:
    #     newLetters.append(getNewLetters(letter, newkey))
    # return "".join(newLetters)

# def getNewLetters(letter, key):
#     newLetterCode = ord(letter) + key
#     return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)

# O(n) time  |  O(n) space
def caesarCipherEncryptor(string, key):
    newLetters = []
    newKey = key % 26
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    for letter in string:
        newLetters.append(getNewletter(letter, newKey, alphabet))
    return "".join(newLetters)

def getNewletter(letter, key, alphabet):
    newLetterCode = alphabet.index(letter) + key
    return alphabet[newLetterCode] if newLetterCode <= 25 else alphabet[-1 + newLetterCode % 25]

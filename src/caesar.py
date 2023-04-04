message = input("enter the message you want to encrypt: ")
message = message.lower()
key = int(input("enter the key: "))


def caesar(alphabet='abcdefghijklmnopqrstuvwxyz'):
    encrypted = ""

    for char in message:
        if char in alphabet:
            index = alphabet.index(char)
            new_index = (index + key) % len(alphabet)
            encrypted += alphabet[new_index]
        else:
            encrypted += char

    return encrypted


print(caesar())

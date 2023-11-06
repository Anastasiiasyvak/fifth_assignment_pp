
def encrypt(rawText, key):
    encryptedText = []
    for char in rawText:
        if char.isupper():
            encryptedText.append(chr((ord(char) + key - 65) % 26 + 65))
        elif char.islower():
            encryptedText.append(chr((ord(char) + key - 97) % 26 + 97))
        else:
            encryptedText.append(char)
    return ''.join(encryptedText)


def decrypt(encryptedText, key1):
    key1 = key1 % 26
    decryptedText = []
    for char in encryptedText:
        if char.isupper():
            decryptedText.append(chr((ord(char) - key1 - 65 + 26) % 26 + 65))
        elif char.islower():
            decryptedText.append(chr((ord(char) - key1 - 97 + 26) % 26 + 97))
        else:
            decryptedText.append(char)
    return ''.join(decryptedText)


def main():
    encryptedText = ""
    while True:
        command = int(input("\nChoose the command:\n1 - encrypt command\n2 - decrypt command\n"))

        if command == 1:
            rawText = input("Enter the rawText:\n")
            key = int(input("Enter your key:\n"))
            print("Text:", rawText)
            print("Key:", key)
            encryptedText = encrypt(rawText, key)
            print("Encrypted text:", encryptedText)

        elif command == 2:
            if encryptedText:
                key1 = int(input("Enter key for decrypting:\n"))
                decryptedText = decrypt(encryptedText, key1)
                print("Decrypted text:", decryptedText)
            else:
                print("No encrypted text to decrypt.")

        else:
            print("Invalid command.")


main()

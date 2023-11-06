
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
        choice = int(input("\nChoose an option:\n1 - Encrypt, decrypt text in console\n2 - Encrypt/Decrypt text to/from a file\n"))
        if choice == 1:
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

        elif choice == 2:
            sub_choice = int(input("Choose an option:\n1 - Encrypt text into a file\n2 - Decrypt text from a file\n"))

            if sub_choice == 1:
                key = int(input("Enter your key:\n"))
                input_file_name = input("Enter the input file name:\n")
                output_file_name = input("Enter the output file name:\n")

                with open(input_file_name, 'r') as input_file:
                    rawText = input_file.read()

                encryptedText = encrypt(rawText, key)

                with open(output_file_name, 'w') as output_file:
                    output_file.write(encryptedText)

                print("Encrypted text has been written to the output file:", output_file_name)

            elif sub_choice == 2:
                key1 = int(input("Enter key for decrypting:\n"))
                input_file_name = input("Enter the input file name:\n")
                output_file_name = input("Enter the output file name:\n")

                with open(input_file_name, 'r') as input_file:
                    encryptedText = input_file.read()

                decryptedText = decrypt(encryptedText, key1)

                with open(output_file_name, 'w') as output_file:
                    output_file.write(decryptedText)

                print("Decrypted text has been written to the output file:", output_file_name)

            else:
                print("Invalid sub-choice.")

        else:
            print("Invalid choice.")

main()

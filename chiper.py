import random


def generate_key(length):
    key = ""
    for _ in range(length):
        key += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return key


def vigenere_encrypt(plaintext, key):
    key = key * (len(plaintext) // len(key)) + key[:len(plaintext) % len(key)]
    ciphertext = ""

    for i in range(len(plaintext)):
        char_plaintext = plaintext[i]
        char_key = key[i]

        encrypted_char = str((ord(char_plaintext) + ord(char_key)) % 256)
        ciphertext += encrypted_char + " "

    return ciphertext.strip(), key


def vigenere_decrypt(ciphertext, key):
    key = key * (len(ciphertext) // len(key)) + \
        key[:len(ciphertext) % len(key)]
    decrypted_text = ""

    cipher_chars = ciphertext.split()

    for i in range(len(cipher_chars)):
        cipher_char = int(cipher_chars[i])
        char_key = key[i]

        decrypted_char = chr((cipher_char - ord(char_key)) % 256)
        decrypted_text += decrypted_char

    return decrypted_text, key


while True:
    print("\n=== Vigenere Cipher ===")
    choice = input("Choose mode (encrypt/decrypt/exit): ").lower()

    if choice == "exit":
        print("Exiting the program.")
        break

    elif choice in ["encrypt", "decrypt"]:
        plaintext = input("Enter the text: ")
        key_choice = input("Choose key type (manual/random): ").lower()

        if key_choice == "manual":
            key = input("Enter the key: ")
        elif key_choice == "random":
            key_length = len(plaintext)
            key = generate_key(key_length)
            print("Generated Key:", key)
        else:
            print("Invalid key choice. Please choose 'manual' or 'random'.")
            continue

        if not plaintext.isalpha() or not key.isalpha():
            print("Invalid input. Text and key must contain only alphabetic characters.")
            continue

        if choice == "encrypt":
            encrypted_text, used_key = vigenere_encrypt(
                plaintext.upper(), key.upper())
            print("\nEncrypted Text:", encrypted_text)
        else:
            ciphertext = input("Enter the ciphertext: ")
            decrypted_text, used_key = vigenere_decrypt(
                ciphertext, key.upper())
            print("\nDecrypted Text:", decrypted_text)

        show_key = input(
            "Do you want to display the key used? (yes/no): ").lower()
        if show_key == "yes":
            print("Used Key:", used_key)

        repeat = input(
            "Do you want to perform another operation? (yes/no): ").lower()
        if repeat != "yes":
            print("Exiting the program.")
            break

    else:
        print("Invalid choice. Please choose 'encrypt', 'decrypt', or 'exit'.")

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result


def xor_cipher(text, key):
    return ''.join(chr(ord(c) ^ key) for c in text)


def main():
    print("Choose an option:")
    print("1. Encode (Caesar Cipher)")
    print("2. Decode (Caesar Cipher)")
    print("3. Encrypt (XOR Cipher)")
    print("4. Decrypt (XOR Cipher)")

    choice = input("Enter choice (1/2/3/4): ")
    message = input("Enter your message: ")

    if choice == '1':
        shift = int(input("Enter shift value: "))
        print("Encoded message:", caesar_cipher(message, shift))
    elif choice == '2':
        shift = int(input("Enter shift value: "))
        print("Decoded message:", caesar_cipher(message, -shift))
    elif choice == '3':
        key = int(input("Enter key (0-255): "))
        print("Encrypted message:", xor_cipher(message, key))
    elif choice == '4':
        key = int(input("Enter key (0-255): "))
        print("Decrypted message:", xor_cipher(message, key))
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
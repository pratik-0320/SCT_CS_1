def caesar_encrypt(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    while True:
        print("\nChoose an option:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            text = input("Enter text to encrypt: ")
            shift = int(input("Enter shift (e.g., 3): "))
            encrypted = caesar_encrypt(text, shift)
            print("Encrypted Text:", encrypted)

        elif choice == '2':
            text = input("Enter text to decrypt: ")
            shift = int(input("Enter original shift: "))
            decrypted = caesar_decrypt(text, shift)
            print("Decrypted Text:", decrypted)

        elif choice == '3':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


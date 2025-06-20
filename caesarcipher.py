def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Handle uppercase and lowercase letters separately
            start = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - start + shift) % 26 + start)
            encrypted_text += encrypted_char
        else:
            # Leave non-alphabet characters unchanged
            encrypted_text += char
    return encrypted_text


def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)


def main():
    print("=== Caesar Cipher Tool ===")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()
    
    if choice not in ['E', 'D']:
        print("Invalid choice. Please enter E or D.")
        return

    message = input("Enter your message: ")
    
    try:
        shift = int(input("Enter shift value (number): "))
    except ValueError:
        print("Shift must be an integer.")
        return

    if choice == 'E':
        result = caesar_cipher_encrypt(message, shift)
        print(f"Encrypted message: {result}")
    else:
        result = caesar_cipher_decrypt(message, shift)
        print(f"Decrypted message: {result}")


if __name__ == "__main__":
    main()

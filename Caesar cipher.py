def caesar_cipher_encrypt(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        # Encrypt uppercase letters
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase letters
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        # Leave non-alphabetic characters as they are
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        # Decrypt uppercase letters
        if char.isupper():
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        # Decrypt lowercase letters
        elif char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        # Leave non-alphabetic characters as they are
        else:
            decrypted_text += char
    return decrypted_text

def main():
    # Ask user for the message and shift value
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    
    # Encrypt the message
    encrypted_message = caesar_cipher_encrypt(message, shift)
    print(f"Encrypted message: {encrypted_message}")
    
    # Decrypt the message
    decrypted_message = caesar_cipher_decrypt(encrypted_message, shift)
    print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
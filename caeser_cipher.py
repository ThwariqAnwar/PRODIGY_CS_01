def caeser(message, key ,mode= 'encrypt'):
    result = ""

    if mode == 'decrypt' :
        key = -key

    for char in message:
        if char.isalpha(): # Check if the character is a letter
            key_amount = 65 if char.isupper() else 97
            # Perform the shift
            result += chr((ord(char) - key_amount + key) % 26 + key_amount)
        else:
            result += char   # Non-alphabetic characters are not encrypted/decrypted

    return result

def main():
    print("Caesar Cipher Encryption/Decryption Tool")

    while True:
        mode = input ("Do you want to (e)ncrypt or (d)ecrypt a message? (e/d):").lower()
        if mode not in ['e', 'd']:
            print("Invalid option. Please choose  'e' for encryption or 'd' for decryption.")
            continue
        
        message = input("Enter your message: ")
        try:
            key = int(input("Enter the key value to shift (an Integer): "))
        except ValueError:
            print("Invalid key value. Please enter an Interger. ")
            continue
        
        if mode == 'e':
            encrypted_message = caeser(message, key, mode='encrypt')
            print(f"Encrypted message: {encrypted_message}")
        else:
            decrypted_message = caeser(message, key, mode='decrypt')
            print(f"Decrypted message: {decrypted_message}")

        another = input("Do you want to encrypt/decrypt another message ? (y/n): ").lower()
        if another != 'y':
            break
        
if __name__=="__main__":
    main()
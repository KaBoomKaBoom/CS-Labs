def remove_spaces(text):
    return ''.join(text.split())

def char_to_index(c):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return alphabet.index(c)

def index_to_char(index):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return alphabet[index]

def check_key(key):
    if not 0 <= key <= 25:
        print("Invalid key. Key must be between 0 and 25.")
        return False
    return True

def check_text(text):
    if not all(c.isalpha() for c in text):
        print("Invalid text. Text should contain only alphabetic characters.")
        return False
    return True

def encrypt(text, key):
    encrypted_text = ""
    text = remove_spaces(text.upper())  # Convert to upper case and remove spaces

    for c in text:
        indexC = char_to_index(c)
        newIndex = (indexC + key) % 26
        encrypted_text += index_to_char(newIndex)
        
    return encrypted_text

def decrypt(text, key):
    decrypted_text = ""
    text = remove_spaces(text.upper())  # Convert to upper case and remove spaces

    for c in text:
        indexC = char_to_index(c)
        newIndex = (indexC - key) % 26
        decrypted_text += index_to_char(newIndex)
        
    return decrypted_text

def main():
    print("Caesar Cipher for the English alphabet")

    while True:
        operation = input("Choose operation (1 - Encrypt, 2 - Decrypt): ").strip()
        
        if operation not in ['1', '2']:
            print("Invalid operation. Please try again.")
            continue

        text = input("Enter text: ").upper()
        text = remove_spaces(text)
        
        key = int(input("Enter key (between 0 and 25): "))

        if not (check_key(key) and check_text(text)):
            continue

        if operation == '1':
            print("Encrypted text: ", encrypt(text, key))
        else:
            print("Decrypted text: ", decrypt(text, key))

        cont = input("Do you want to perform another operation? (yes/no): ").lower()
        if cont != 'yes':
            break

if __name__ == "__main__":
    main()

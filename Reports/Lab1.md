# **Berco Andrei**  
# **FAF - 221**  

# **Caesar Cipher Implementation Report**

---

## **1. Introduction to Caesar Cipher**

The Caesar cipher is one of the simplest encryption techniques. It is a substitution cipher where each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. This fixed number of positions is called the *key*.

### **Encryption Formula:**
\[
c = (x + k) \% 26
\]
Where:
- \(x\) is the index of the character in the alphabet.
- \(k\) is the key.
- \(\% 26\) ensures wrapping around the alphabet.

### **Decryption Formula:**
\[
m = (y - k) \% 26
\]
Where:
- \(y\) is the index of the cipher character in the alphabet.
- \(k\) is the key.

### **Security Considerations**  
Caesar cipher has a limited keyspace (only 25 possible keys), making it susceptible to brute-force attacks.

### **Example:**
Encrypting `"HELLO"` with a key \(k = 3\) gives:
- H → K
- E → H
- L → O
- O → R

Result: `"KHOOR"`

---

## **2. Task 1: Basic Caesar Cipher Implementation**

### **Task Description**  
The goal of this task is to implement the Caesar cipher for the English alphabet, handling only uppercase letters (`A-Z`) and ignoring spaces. The program should allow the user to encrypt or decrypt text based on a chosen key.

### **Code Implementation**

#### **Key Functions:**
```python
def char_to_index(c):
    return ord(c) - ord('A')

def index_to_char(i):
    return chr(i + ord('A'))
```
These functions convert characters to and from their indices in the alphabet, enabling the Caesar shift.

#### **Encrypt Function:**
```python
def encrypt(text, key):
    encrypted_text = ""
    for c in text:
        indexC = char_to_index(c)
        newIndex = (indexC + key) % 26
        encrypted_text += index_to_char(newIndex)
    return encrypted_text
```
- Shifts each character in the text by the given key.

#### **Decrypt Function:**
```python
def decrypt(text, key):
    decrypted_text = ""
    for c in text:
        indexC = char_to_index(c)
        newIndex = (indexC - key) % 26
        decrypted_text += index_to_char(newIndex)
    return decrypted_text
```
- Reverses the encryption process using the same key.

#### **Key Validation:**
```python
def check_key(key):
    if key < 0 or key > 25:
        print("Invalid key")
        return False
    return True
```
Ensures the key is between 0 and 25.

### **Running the Task:**
The `mainTask1()` function allows the user to select an operation (encryption or decryption), input the text and key, and then see the result.

```python
def mainTask1():
    while True:
        print("1. Encrypt text\n2. Decrypt text")
        operation = input("Choose an operation: ")

        if operation == "1":
            text = input("Enter text to encrypt: ").upper().replace(" ", "")
            key = int(input("Enter key: "))
            if check_key(key) and all(c.isalpha() for c in text):
                print("Encrypted text:", encrypt(text, key))
        elif operation == "2":
            text = input("Enter text to decrypt: ").upper().replace(" ", "")
            key = int(input("Enter key: "))
            if check_key(key) and all(c.isalpha() for c in text):
                print("Decrypted text:", decrypt(text, key))
```

---

## **3. Task 2: Caesar Cipher with Two Keys**

### **Task Description**  
To enhance the security of the basic Caesar cipher, a second key (`k2`) is introduced. This key is a permutation of the alphabet generated from a user-provided keyword. The additional key increases security, making it more difficult for an attacker to brute force the cipher.

### **Code Implementation**

#### **Creating the Permuted Alphabet:**
```python
def create_permuted_alphabet(keyword):
    keyword = ''.join(sorted(set(keyword), key=keyword.index))  # Remove duplicates
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    permuted_alphabet = keyword + ''.join([ch for ch in alphabet if ch not in keyword])
    return permuted_alphabet
```
- Generates a new alphabet using the keyword by removing duplicate letters and preserving order.

#### **Encrypt Function (Two Keys):**
```python
def encrypt(text, k1, k2):
    encrypted_text = ""
    text = text.upper().replace(' ', '')
    permuted_alphabet = create_permuted_alphabet(k2)

    for c in text:
        if c in permuted_alphabet:
            indexC = char_to_index(c)
            newIndex = (indexC + k1) % 26
            encrypted_text += permuted_alphabet[newIndex]
    return encrypted_text
```
- Encrypts text using both `k1` (shift) and `k2` (permuted alphabet).

#### **Decrypt Function (Two Keys):**
```python
def decrypt(text, k1, k2):
    decrypted_text = ""
    text = text.upper().replace(' ', '')
    permuted_alphabet = create_permuted_alphabet(k2)

    for c in text:
        if c in permuted_alphabet:
            indexC = permuted_alphabet.index(c)
            newIndex = (indexC - k1) % 26
            decrypted_text += index_to_char(newIndex)
    return decrypted_text
```
- Reverses the encryption using both `k1` and `k2`.

### **Running the Task:**
The `main()` function allows the user to input both the Caesar shift key (`k1`) and a keyword for the permuted alphabet (`k2`), and choose whether to encrypt or decrypt.

```python
def main():
    while True:
        operation = input("1 to encrypt, 2 to decrypt: ").strip()
        if operation not in ['1', '2']:
            continue
        
        k1 = int(input("Enter Caesar shift key: "))
        k2 = input("Enter keyword: ").upper()
        
        message = input("Enter message: ").upper().replace(" ", "")
        
        if operation == "1":
            print("Encrypted text:", encrypt(message, k1, k2))
        else:
            print("Decrypted text:", decrypt(message, k1, k2))
```

---

## **4. Conclusion**

- **Task 1**: Implemented a basic Caesar cipher for encryption and decryption using a single key.
- **Task 2**: Improved the cipher's security by introducing a second key, `k2`, which permutes the alphabet, making it more resistant to brute force attacks.  

Both tasks adhered to modular arithmetic principles and handled input validation to ensure the operations ran correctly.

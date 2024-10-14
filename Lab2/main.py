import string
from collections import Counter
import matplotlib.pyplot as plt

ciphertext = input("Enter the ciphertext: ")
# Frequency of letters in English
english_letter_frequency = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'C', 'U', 'M', 'W', 'F', 'G', 'Y', 'P', 'B', 'V', 'K', 'J', 'X', 'Q', 'Z']

# Remove non-alphabetic characters and convert to uppercase
def preprocess_text(text):
    return ''.join([char for char in text.upper() if char in string.ascii_uppercase])

# Function to analyze frequency of letters in the ciphertext
def frequency_analysis(text):
    return Counter(text)

# Function to create substitution mapping based on frequency analysis
def create_substitution_mapping(ciphertext, english_freq):
    # Preprocess text
    cleaned_text = preprocess_text(ciphertext)
    
    # Get frequency of letters in the ciphertext
    cipher_letter_frequency = frequency_analysis(cleaned_text)
    
    # Sort the ciphertext letters by frequency in descending order
    sorted_cipher_letters = [item[0] for item in cipher_letter_frequency.most_common()]
    
    # Create a mapping from the sorted ciphertext letters to the most frequent English letters
    substitution_mapping = {sorted_cipher_letters[i]: english_freq[i] for i in range(2)}
    
    return substitution_mapping

# Function to decrypt the ciphertext using the substitution mapping
def decrypt_with_mapping(ciphertext, substitution_mapping):
    decrypted_text = ''
    for char in ciphertext:
        if char.upper() in substitution_mapping:
            decrypted_char = substitution_mapping[char.upper()]
            # Substituted characters in uppercase, non-substituted in lowercase
            decrypted_text += decrypted_char.upper()
        else:
            # Leave non-alphabetic and non-substituted characters unchanged and lowercase
            decrypted_text += char.lower() if char in string.ascii_lowercase else char
    return decrypted_text

def add_mapping(substitution_mapping, cipher_char, english_char):
    # Add a new mapping for the given cipher character
    substitution_mapping[cipher_char] = english_char
    return substitution_mapping


# Function to plot letter frequencies
def plot_letter_frequencies(counter):
    letters = sorted(counter.keys())
    frequencies = [counter[letter] for letter in letters]
    
    plt.bar(letters, frequencies, color='blue')
    plt.xlabel('Letters')
    plt.ylabel('Frequency')
    plt.title('Letter Frequency Analysis')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

# Frequency of letters in the ciphertext for plotting
cipher_cleaned_text = preprocess_text(ciphertext)
cipher_letter_count = frequency_analysis(cipher_cleaned_text)

# Plotting the frequency
plot_letter_frequencies(cipher_letter_count)

# Substitution mapping based on frequency analysis
substitution_mapping = create_substitution_mapping(ciphertext, english_letter_frequency)

# Decrypt the ciphertext
decrypted_text = decrypt_with_mapping(ciphertext, substitution_mapping)
print("\nSubstitution Mapping:", substitution_mapping)
print("Decrypted Text After First Substitution:\n", decrypted_text)

add_mapping(substitution_mapping, 'Q', 'H')
add_mapping(substitution_mapping, 'T', 'A')

decrypted_text = decrypt_with_mapping(ciphertext, substitution_mapping)
print("\nDecrypted Text After First Substitution:\n", decrypted_text)

add_mapping(substitution_mapping, 'R', 'W')
add_mapping(substitution_mapping, 'I', 'R')
add_mapping(substitution_mapping, 'F', 'Y')
add_mapping(substitution_mapping, 'Z', 'M')
add_mapping(substitution_mapping, 'S', 'L')
add_mapping(substitution_mapping, 'N', 'O')

decrypted_text = decrypt_with_mapping(ciphertext, substitution_mapping)
print("\nDecrypted Text After First Substitution:\n", decrypted_text)

add_mapping(substitution_mapping, 'G', 'N')
add_mapping(substitution_mapping, 'P', 'S')
add_mapping(substitution_mapping, 'K', 'V')
add_mapping(substitution_mapping, 'X', 'I')
add_mapping(substitution_mapping, 'O', 'D')
add_mapping(substitution_mapping, 'H', 'C')
add_mapping(substitution_mapping, 'L', 'K')

decrypted_text = decrypt_with_mapping(ciphertext, substitution_mapping)
print("\nDecrypted Text After First Substitution:\n", decrypted_text)


add_mapping(substitution_mapping, 'C', 'F')
add_mapping(substitution_mapping, 'A', 'B')
add_mapping(substitution_mapping, 'D', 'U')
add_mapping(substitution_mapping, 'J', 'G')
add_mapping(substitution_mapping, 'U', 'P')
add_mapping(substitution_mapping, 'M', 'Z')
add_mapping(substitution_mapping, 'Y', 'X')
add_mapping(substitution_mapping, 'B', 'Q')


decrypted_text = decrypt_with_mapping(ciphertext, substitution_mapping)
print("\nSubstitution Mapping:", substitution_mapping)
print("Final Decrypted Text:\n", decrypted_text)
class AnalyzeFrequency():
    def __init__(self, text):
        self.text = text
    # Remove non-alphabetic characters and convert to uppercase
    def preprocess_text(self,ciphertext):
        return ''.join([char for char in ciphertext.upper() if char in string.ascii_uppercase])

    # Function to analyze frequency of letters in the ciphertext
    def frequency_analysis(self, ciphertext):
        return Counter(ciphertext)

    # Function to create substitution mapping based on frequency analysis
    def create_substitution_mapping(string: ciphertext, english_freq):
        # Preprocess text
        cleaned_text = ''.join([char for char in ciphertext() if char in string.ascii_uppercase])
        
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
                # Preserve case
                decrypted_text += decrypted_char.lower() if char.islower() else decrypted_char
            else:
                decrypted_text += char  # Leave non-alphabetic characters unchanged
        return decrypted_text


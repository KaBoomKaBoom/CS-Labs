import string
from collections import Counter
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Entry, Button, Text, END, messagebox

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
    cleaned_text = preprocess_text(ciphertext)
    cipher_letter_frequency = frequency_analysis(cleaned_text)
    sorted_cipher_letters = [item[0] for item in cipher_letter_frequency.most_common()]
    substitution_mapping = {sorted_cipher_letters[i]: english_freq[i] for i in range(len(sorted_cipher_letters))}
    return substitution_mapping

# Function to decrypt the ciphertext using the substitution mapping
def decrypt_with_mapping(ciphertext, substitution_mapping):
    decrypted_text = ''
    for char in ciphertext:
        if char.upper() in substitution_mapping:
            decrypted_char = substitution_mapping[char.upper()]
            decrypted_text += decrypted_char.upper()
        else:
            decrypted_text += char.lower() if char in string.ascii_lowercase else char
    return decrypted_text

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

# GUI Setup
def run_gui():
    # Create the main window
    root = Tk()
    root.title("Caesar Cipher Decryptor")
    root.geometry("900x700")
    
    # Global variable for substitution mapping
    global substitution_mapping
    substitution_mapping = {}

    # Define input fields and labels
    Label(root, text="Enter the ciphertext:").pack()
    input_text = Text(root, height=4, width=70)
    input_text.pack()

    # Labels and input fields for substitutions
    Label(root, text="Add a substitution (Cipher -> Plain):").pack(pady=5)
    cipher_char_entry = Entry(root, width=5)
    cipher_char_entry.pack(side="left", padx=5)
    Label(root, text="->").pack(side="left")
    plain_char_entry = Entry(root, width=5)
    plain_char_entry.pack(side="left", padx=5)
    
    # Output Text Area for Decrypted Text
    Label(root, text="Decrypted Text:").pack(pady=5)
    output_text = Text(root, wrap='word', height=10, width=70)
    output_text.pack()

    # Output Text Area for Substitution Mappings
    Label(root, text="Current Substitution Mappings:").pack(pady=5)
    mapping_text = Text(root, wrap='word', height=10, width=70)
    mapping_text.pack()

    # Function to analyze frequency and display it
    def analyze_frequency():
        ciphertext = input_text.get("1.0", END)
        cipher_cleaned_text = preprocess_text(ciphertext)
        cipher_letter_count = frequency_analysis(cipher_cleaned_text)
        plot_letter_frequencies(cipher_letter_count)
    
    # Function to decrypt the text and display it
    def decrypt_text():
        ciphertext = input_text.get("1.0", END)
        decrypted = decrypt_with_mapping(ciphertext, substitution_mapping)
        output_text.delete(1.0, END)
        output_text.insert(END, f"Decrypted Text:\n{decrypted}\n")

    # Function to update the mapping display
    def update_mapping_display():
        mapping_text.delete(1.0, END)
        for cipher_char, plain_char in substitution_mapping.items():
            mapping_text.insert(END, f"{cipher_char} -> {plain_char}\n")

    # Function to add new mapping
    def add_mapping():
        cipher_char = cipher_char_entry.get().upper()
        plain_char = plain_char_entry.get().upper()
        if cipher_char and plain_char and len(cipher_char) == 1 and len(plain_char) == 1:
            substitution_mapping[cipher_char] = plain_char
            update_mapping_display()
            messagebox.showinfo("Mapping Added", f"Mapping {cipher_char} -> {plain_char} added.")
            cipher_char_entry.delete(0, END)
            plain_char_entry.delete(0, END)
        else:
            messagebox.showerror("Error", "Please enter valid characters for both fields.")

    # Buttons for frequency analysis, decryption, and adding mappings
    Button(root, text="Analyze Frequency", command=analyze_frequency).pack(pady=5)
    Button(root, text="Add Substitution", command=add_mapping).pack(pady=5)
    Button(root, text="Decrypt Text", command=decrypt_text).pack(pady=5)

    # Run the GUI loop
    root.mainloop()

# Run the GUI
if __name__ == '__main__':
    run_gui()

import string
import random

class TextPreparation:

    def remove_punctuation(self, text):
        return text.translate(str.maketrans('', '', string.punctuation)).replace(" ", "").upper().replace("J", "I")
    
    
    def insert_additional_char(self, text):
        for i in range(0, len(text) - 1):
            if text[i] == text[i+1]:
                text = text[:i+1] + "X" + text[i+1:]
        if len(text) % 2 != 0:
            text += "X"
        return text
    
    
    def split_text_in_pairs(self, text):
        splited_text = ""
        i = 0
        for char in text:
            splited_text += char
            i+=1
            if i % 2 == 0:
                splited_text += " "
        return splited_text
    
    
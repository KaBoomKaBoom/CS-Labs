import numpy as np

class Matrix:
    def __init__(self, key):
        self.key = key
        
    def prepare_key(self):
        used_letters = []
        return "".join([char for char in self.key if char not in used_letters and not used_letters.append(char)]).replace(" ", "").upper()
    
    def construct_matrix(self):
        key = self.prepare_key()
        alphabet = "AĂÂBCDEFGHIÎKLMNOPQRSȘTȚUVWXYZ"
        matrix = np.zeros((6,5), dtype=str)
        
        for i in range(6):
            for j in range(5):
                if i*5+j < len(key):
                    matrix[i][j] = key[i*5+j]
                else:
                    for char in alphabet:
                        if char not in key:
                            matrix[i][j] = char
                            alphabet = alphabet.replace(char, "")
                            break
        return matrix
    
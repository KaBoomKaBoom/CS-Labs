from numpy import matrix


class CryptoService:
    
    def __init__(self, text, crypto_matrix):
        self.text = text
        self.crypto_matrix = crypto_matrix
        
    def get_position(self, char):
        for i in range(6):
            for j in range(5):
                if self.crypto_matrix[i][j] == char:
                    return i, j
        return None, None
        
    def encrypt(self):
        encrypted_text = ""
        for i in range(0, len(self.text), 3):
            first_letter = self.text[i]
            second_letter = self.text[i+1]
            
            first_letter_position = self.get_position(first_letter)
            second_letter_position = self.get_position(second_letter)
            # print("First letter: ", first_letter, " position: ", first_letter_position)
            # print("Second letter: ", second_letter, " position: ", second_letter_position)
            
            #Same line
            if first_letter_position[0] == second_letter_position[0]:
                encrypted_text += self.crypto_matrix[first_letter_position[0]][(first_letter_position[1]+1)%5]
                encrypted_text += self.crypto_matrix[second_letter_position[0]][(second_letter_position[1]+1)%5]
                
            #Same column
            elif first_letter_position[1] == second_letter_position[1]:
                encrypted_text += self.crypto_matrix[(first_letter_position[0]+1)%6][first_letter_position[1]]
                encrypted_text += self.crypto_matrix[(second_letter_position[0]+1)%6][second_letter_position[1]]
                
            #Rectangle
            else:
                encrypted_text += self.crypto_matrix[first_letter_position[0]][second_letter_position[1]]
                encrypted_text += self.crypto_matrix[second_letter_position[0]][first_letter_position[1]]   

        return encrypted_text
    
    def decrypt(self):
        decrypted_text = ""
        for i in range(0, len(self.text), 3):
            first_letter = self.text[i]
            second_letter = self.text[i+1]
            
            first_letter_position = self.get_position(first_letter)
            second_letter_position = self.get_position(second_letter)
            # print("First letter: ", first_letter, " position: ", first_letter_position)
            # print("Second letter: ", second_letter, " position: ", second_letter_position)
            
            #Same line
            if first_letter_position[0] == second_letter_position[0]:
                decrypted_text += self.crypto_matrix[first_letter_position[0]][(first_letter_position[1]-1)%5]
                decrypted_text += self.crypto_matrix[second_letter_position[0]][(second_letter_position[1]-1)%5]
                
            #Same column
            elif first_letter_position[1] == second_letter_position[1]:
                decrypted_text += self.crypto_matrix[(first_letter_position[0]-1)%6][first_letter_position[1]]
                decrypted_text += self.crypto_matrix[(second_letter_position[0]-1)%6][second_letter_position[1]]
                
            #Rectangle
            else:
                decrypted_text += self.crypto_matrix[first_letter_position[0]][second_letter_position[1]]
                decrypted_text += self.crypto_matrix[second_letter_position[0]][first_letter_position[1]]   

        return decrypted_text
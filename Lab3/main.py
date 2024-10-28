import TextPreparation
import Matrix
import CryptoService

#dacă cele două litere sunt în linii și coloane diferite, decriptarea se face exact la fel ca și criptarea

text_preparation = TextPreparation.TextPreparation()

while True:
    print("\n1. Encrypt\n2. Decrypt\n3. Exit")
    option = input("Choose an option: ")
    if option == "1":
        text_to_encrypt = input("Messag to encrypt: ")
        key = input("Key: ")
        prepared_text = text_preparation.remove_punctuation(text_to_encrypt)
        prepared_text = text_preparation.insert_additional_char(prepared_text)
        prepared_text = text_preparation.split_text_in_pairs(prepared_text)
        print("\nPrepared text: ", prepared_text)
        
        
        key = Matrix.Matrix(key).prepare_key()
        if len(key) < 7:
            print("Key must have at least 7 characters!")
        else:
            matrix = Matrix.Matrix(key).construct_matrix()
            print("\nMatrix: \n", matrix)
            
            print("\nEcripted text: \n", CryptoService.CryptoService(prepared_text, matrix).encrypt())
        
    elif option == "2":
        text_to_decrypt = input("Messag to decrypt: ")
        text_to_decrypt = text_preparation.split_text_in_pairs(text_to_decrypt)
        
        key = input("Key: ")
        if len(key) < 7:
            print("Key must have at least 7 characters!")
        else:
            key = Matrix.Matrix(key).prepare_key()
            matrix = Matrix.Matrix(key).construct_matrix()
            
            print("Decrypted text: \n", CryptoService.CryptoService(text_to_decrypt, matrix).decrypt())
    
    elif option == "3":
        break
    
    else:
        print("Invalid option!")
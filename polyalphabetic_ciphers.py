import random

class Polyalphabetic_Ciphers:
    """A class implementing polyalphabetic substitution ciphers, currently supporting the Vigenère cipher.
    
    The Vigenère cipher is a polyalphabetic substitution cipher that uses a keyword to encrypt
    plaintext. Each letter of the keyword is used to shift the plaintext letters by different amounts.
    """
    
    def __init__(self):
        
        self.letter_to_number = { # Maps each uppercase letter to its position (0-25) in the alphabet
            "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5,
            "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11,
            "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17,
            "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23,
            "Y": 24, "Z": 25
        }
        
        self.input_text: str = ""
        self.input_key: str = ""
        self.encrypted_final_text: str = ""
        self.decrypted_final_text: str = ""

# helping methods
    def produce_full_length_key(self) -> str:
        """
        Makes the length of the key same as the length of the plain text
        """
        # Generate a key of the same length as the input text by repeating the key
        full_length_key: str = ""
        for n in range(len(self.input_text)):
            full_length_key += self.input_key[n % len(self.input_key)]

        return full_length_key

    def produce_random_key(self) -> str:
        """
        produces a random key with the same length as the input text
        """

        random_key: str = ""
        for _ in range(len(self.input_text)):
            random_key += random.choice(list(self.letter_to_number.keys()))
        
        return random_key

    def number_to_letter(self, letter: int) -> str:
        """
        Convert the resulting number back to a letter
        """

        decrypted: str = ""
        decrypted += list(self.letter_to_number.keys())[
            list(self.letter_to_number.values()).index(letter)
        ]

        return decrypted 

# encryption methods
    def vigenere_cipher(self) -> str:
        """Implements the Vigenère cipher encryption algorithm.
        
        Returns:
            str: The encrypted text using the Vigenère cipher
        """
        self.encrypted_final_text = ""
        key = self.produce_full_length_key()

        # Encrypt each character using the corresponding key character
        for i in range(len(self.input_text)):

            # Add the numeric values of the current input and key letters
            new_letter_no: int = (self.letter_to_number[self.input_text[i]] + 
                           self.letter_to_number[key[i]]) % 26
            
            self.encrypted_final_text += self.number_to_letter(new_letter_no)
            
        return self.encrypted_final_text

    def vernam_cipher(self) -> str:

        self.encrypted_final_text = ""
        key = self.produce_random_key()

        for i in range(len(self.input_text)):

            new_letter: int = (self.letter_to_number[self.input_text[i]]^self.letter_to_number[key[i]]) % 26
            
            self.encrypted_final_text += self.number_to_letter(new_letter)
        
        return self.encrypted_final_text

    def encrypt(self, encryption_method: str) -> str:
        """Encrypts the input text using the specified encryption method.
        
        Args:
            encryption_method (str): The name of the encryption method to use
            
        Returns:
            str: The encrypted text
        """
        encryption_method_function = getattr(self, encryption_method, None)
        self.encrypted_final_text = encryption_method_function()
        return self.encrypted_final_text

# decryption methods
    def crack_polyalphabetic_cipher(self) -> str:

        key = self.produce_full_length_key()

        for i in range(len(self.input_text)):
            old_letter_no: int = (self.letter_to_number[self.input_text[i]]-self.letter_to_number[key[i]])
            if old_letter_no < 0:
                old_letter_no += 26

            self.decrypted_final_text += self.number_to_letter(old_letter_no)

        return self.decrypted_final_text

    def decrypt(self, decryption_method: str) -> str:

        decryption_method_function = getattr(self, decryption_method, None)

        self.decrypted_final_text = decryption_method_function()

        return self.decrypted_final_text




# Example usage

"""cipher = Polyalphabetic_Ciphers()
cipher.input_text = "hello".upper()
result = cipher.encrypt("vernam_cipher")
print(result) 

cipher.input_text = result.upper()
result = cipher.crack_vernam_cipher()  
print(result)"""

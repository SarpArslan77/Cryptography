class Polyalphabetic_Ciphers():
    def __init__(self):
        self.letter_to_number: dict = {                    # maps each uppercase letter to its position (0-25) in the alphabet
            "A":0, "B":1, "C":2, "D":3, "E":4, "F":5,
            "G":6, "H":7, "I":8, "J":9, "K":10, "L":11,
            "M":12, "N":13, "O":14, "P":15, "Q":16, "R":17,
            "S":18, "T":19, "U":20, "V":21, "W":22, "X":23,
            "Y":24, "Z":25,
        }

        self.encryption_polyalphabetic_functions: list[str] = ["vigenere_cipher"]    # list of available encryption methods
        self.decryption_polyalphabetic_functions: list[str] = []                     # reserved for future decryption methods

        self.input_text: str = ""              # stores the plaintext to be encrypted
        self.key: str = ""                     # stores the encryption key
        self.encrypted_final_text: str = ""    # stores the resulting ciphertext

    def vigenere_cipher(self) -> str:
        full_length_key: str = ""              # will store the key repeated to match input text length
        
        for n in range(len(self.input_text)):  # extends the key by repeating it to match input length
            full_length_key = full_length_key + self.key[n%len(self.key)]    # uses modulo to wrap around key characters
        
        for n in range(len(self.input_text)):  # process each character of input text
            new_letter_no: int = self.letter_to_number[self.input_text[n]] + self.letter_to_number[full_length_key[n]]    # add values of current input and key letters
            self.encrypted_final_text = self.encrypted_final_text + (        # convert number back to letter using modulo 26
                list(self.letter_to_number.keys())[
                    list(self.letter_to_number.values()).index(new_letter_no%26)
                ]
            )

        return self.encrypted_final_text

    def encrypt(self, encryption_method: str):
        encryption_method_function = getattr(self, encryption_method, None)    # Dynamically get the specified encryption method
        self.encrypted_final_text = encryption_method_function()               # Execute the encryption function
        return self.encrypted_final_text

# Example usage (commented out)
"""
cipher = Polyalphabetic_Ciphers()
cipher.input_text = "HELLO"          # Set the plaintext to encrypt
cipher.key = "KEY"                   # Set the encryption key
result = cipher.encrypt("vigenere_cipher")
print(result)                        # Would print the encrypted result
"""
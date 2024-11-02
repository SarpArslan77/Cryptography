import random

#TODO: learn and add frequency analysis

# different type of substition ciphers
class Substition_Ciphers():

    def __init__(self):

        # all uppercase letters from the english dictionary
        self.uppercase_letters: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        # a dictionary to change the letters with substitioned letters
        self.encryption_letter_mapping: dict = {}

        # a text, to be inputted from the user in order to be encrypted
        self.encryption_text: str = ""

        # an encyrpted text, with an given text and method 
        self.encrypted_final_text: str = ""

        # a encryption method, to be inputted from the user
        self.encryption_method: str = ""

        # all the possible encryption functions for the Substition_Cipher
        self.all_encryption_functions: list[str] = ["caeser_cipher", "random_substition"]

        #a dictionary to change the substitioned letters with normal letters
        self.decryption_letter_mapping: dict = {}

        #an decypted text, with an given text and method 
        self.decrypted_final_text: list[str] = []

        # a text, to be inputted from the user in order to be decrypted
        self.decryption_text: str = ""

        # a decryption method, to be inputted from the user
        self.decryption_method: str = ""

        # all the possible decryption functions for the Substition_Cipher
        self.all_decryption_functions: list[str] = ["brute_force_caesers_cipher"]

    def encrypt(self, encryption_method: str, input_text: str) -> str:
        """Encrypts the input text using the selected encryption method.

        Returns:
            str: The encrypted text produced by the selected method.
        """
        #*getattr(object, attribute_name, default_value)
        #*  object: The object from which to retrieve the attribute.
        #*  attribute_name: The name of the attribute you want to retrieve (passed as a string).
        #*  default_value (optional): The value returned if the attribute doesn't exist. If not provided and the attribute is missing, an AttributeError will be raised.

        self.encryption_text = input_text

        encryption_method_function = getattr(self, encryption_method, None)

        # use the given method to encrypt the text
        self.encrypted_text = encryption_method_function()

        return self.encrypted_text

    def caeser_cipher(self, shifting_amount: int = 3)  -> str:

        # shift the alphabet according to amount(factually in ceasers cipher is shifting amount 3)
        for _ in range(shifting_amount):
            substitution_letters = self.uppercase_letters[-1] + self.uppercase_letters[:-1]

        # uppercase all the text for better readablity
        self.text = self.encryption_text.upper()

        # add all the substituted letters to a dict with corresponding letters in a normal alphabet
        for _ in range(len(substitution_letters)):
            self.encryption_letter_mapping[self.uppercase_letters[_]] = substitution_letters[_]

        # also add the case for a space
        self.encryption_letter_mapping[" "] = " "

        # create the substituted cipher
        result = ''.join(self.encryption_letter_mapping[char] for char in self.text)

        return result

    def random_substition(self) -> str:

        # turn the self.uppercase_letters str to a list format
        randomized_letters = list(self.uppercase_letters)


        # randomize the order of the letters for a random substition
        random.shuffle(randomized_letters) 

        # uppercase all the text for better readablity
        self.encryption_text = self.encryption_text.upper()

        # add all the substituted letters to a dict with corresponding letters in a normal alphabet
        for _ in range(len(randomized_letters)):
            self.encryption_letter_mapping[self.uppercase_letters[_]] = randomized_letters[_]

        # also add the case for a space
        self.encryption_letter_mapping[" "] = " "

        # create the substituted cipher
        self.encrypted_final_text = ''.join(self.encryption_letter_mapping[char] for char in self.encryption_text)

        return self.encrypted_final_text

    def decrypt(self, decryption_method: str, input_text: str) -> str:

        self.decryption_text = input_text

        # turns a str into a function
        decryption_method_function = getattr(self, decryption_method, None)

        # print all the possibilities with the determined method of decryption
        self.decrypted_final_text = decryption_method_function()

        return self.decrypted_final_text

    def brute_force_caesers_cipher(self) -> list[str]:
        """Attempts to decrypt the encrypted text by trying all possible shifts for Caesar's cipher.

        Appends the decrypted text for each shift to `self.decrypted_final_text`.

        """
        # Reset the list of decrypted texts
        self.decrypted_final_text = []
        
        # Loop through all possible shifts (0 to 25)
        for shift in range(26):
            # Reset the decryption mapping for each new shift
            self.decryption_letter_mapping = {}
            
            # Create the mapping for the current shift
            for i in range(26):
                original_index = (i + shift) % 26
                encrypted_letter = self.uppercase_letters[i]
                decrypted_letter = self.uppercase_letters[original_index]
                self.decryption_letter_mapping[encrypted_letter] = decrypted_letter
            
            # Add space and handle non-alphabetic characters by leaving them unchanged
            self.decryption_letter_mapping[' '] = ' '
            
            # Decrypt the text using current mapping
            decrypted_final_text_example = ''.join(
                self.decryption_letter_mapping.get(char, char)  # Keep non-mapped chars unchanged
                for char in self.decryption_text.upper()
            )

            # output the result 
            self.decrypted_final_text.append(decrypted_final_text_example)

        return self.decrypted_final_text












































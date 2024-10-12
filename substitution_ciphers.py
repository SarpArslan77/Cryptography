from nltk.corpus import words
import random

#TODO: learn and add frequency analysis

# different type of substition ciphers
class Substition_Ciphers():

    def __init__(self):


        #  all the gramatically correct english words
        self.words: list[str] = words.words()

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

        # language of the decryption
        self.decryption_language: str = None

    def check_input_text(self) -> bool:
        """Prompts the user to input a text to encrypt and checks if all words are valid English words.

        Returns:
            bool: True if all words are valid English words; otherwise, continues to prompt the user.
        """
        # loop doesn't end, until all the words are english
        is_text: bool = False

        while not(is_text):

            # get the text as a input from the user
            self.encryption_text: str = input("Write a text to encrypt : ")

            # assume that the text is true(if not, the loop continues)
            is_text = True

            # seperate the words in a text and add them to a list[str]
            seperate_words: list[str] = self.encryption_text.split()

            # check, whether all words are indeed english words
            for word in seperate_words:
                if word not in self.words:
                    print("The text consist foreign/unknown words, please write a text only consisting of english words")
                    print()
                    is_text = False
                    continue
        
        return True

    def check_encryption_method(self) -> bool:
        """Prompts the user to select an encryption method from the available methods and checks if the input is valid.

        Returns:
            bool: True if the selected method is valid; otherwise, continues to prompt the user.
        """
        # loop doesn't end, until the method is present in the functions of this class(self.all_encryption_functions)
        is_method: bool = False

        while not(is_method):

            print()

            # write all the possible functions to user, to choose from
            [print(function) for function in self.all_encryption_functions]
            print("--------------------------------")

            # get the method as a input from the user
            self.encryption_method: str = input("Write a method to use for encryption(possible methods are listed above): ")
            print()

            # assume that, the given method is present in the functions
            is_method = True

            # check, whether the method is actually present, if not ask again
            if self.encryption_method not in self.all_encryption_functions:
                print("The method is not embedded in this class, so it can not be called. Please give an appropiate Method")
                is_method = False

        return True

    def check_decrypted_text(self) -> bool:
        """Checks if the decrypted text consists entirely of valid English words.

        Returns:
            bool: True if all words in the decrypted text are valid; False otherwise.
        """
        # seperate the words in a text and add them to a list[str]
        #*  The list comprehension automatically collects these lowercase words into a new list 
        #*   without needing to explicitly use append(). The list comprehension does the work of creating a new list behind the scenes.
        separate_words: list[str] = [word.lower() for word in self.decrypted_final_text.split()]

        # checks whether the text makes sense
        for word in separate_words:
            if word not in self.words:
                return False
        
        # if it makes sense, return a "True" boolean
        return True

    def check_decryption_method(self) -> bool:
        """Prompts the user to select an decryption method from the available methods and checks if the input is valid.

        Returns:
            bool: True if the selected method is valid; otherwise, continues to prompt the user.
        """
        # loop doesn't end, until the method is present in the functions of this class(self.all_decryption_functions)
        is_method: bool = False

        while not(is_method):

            print()

            # write all the possible functions to user, to choose from
            [print(function) for function in self.all_decryption_functions]
            print("--------------------------------")

            # get the method as a input from the user
            self.decryption_method: str = input("Write a method to use for decryption(possible methods are listed above): ")
            print()

            # assume that, the given method is present in the functions
            is_method = True

            # check, whether the method is actually present, if not ask again
            if self.decryption_method not in self.all_decryption_functions:
                print("The method is not embedded in this class, so it can not be called. Please give an appropiate Method")
                is_method = False

        return True        
    
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
        Only appends valid English words when `decryption_language` is set to 'English'.
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

            # Handle different language decryption strategies
            if self.decryption_language == "Default":
                self.decrypted_final_text.append(decrypted_final_text_example)
            elif self.decryption_language == "English":
                # Split the decrypted text into words and check if all words are valid
                words_in_text = decrypted_final_text_example.split()
                for word in words_in_text:
                    word = word.lower()
                    if word in self.words:
                        word = word.upper()
                        self.decrypted_final_text.append(word)
                        
        return self.decrypted_final_text












































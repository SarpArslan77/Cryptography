from nltk.corpus import words



# different type of substition ciphers
class Substition_Ciphers:

    def __init__(self):

        #  all the gramatically correct english words
        self.words: list[str] = words.words()

        # all uppercase letters from the english dictionary
        self.uppercase_letters: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        # a dictionary to change the letters with substitioned letters
        self.letter_mapping: dict = {}

        # a text, to be inputted from the user
        self.text: str = ""

        self.method: str = ""
        self.all_functions: list[str] = ["caesers_cipher"]


    def check_text(self) -> bool:

        # loop doesn't end, until all the words are english
        is_text: bool = False

        while not(is_text):

            # get the text as a input from the user
            self.text: str = input("Write a text to encrypt : ")

            # assume that the text is true(if not, the loop continues)
            is_text = True

            # seperate the words in a text and add them to a list[str]
            seperate_words: list[str] = self.text.split()

            # check, whether all words are indeed english words
            for word in seperate_words:
                if word not in self.words:
                    print("The text consist foreign/unknown words, please write a text only consisting of english words")
                    print()
                    is_text = False
                    continue
        
        return True

    def check_method(self) -> bool:

        # loop doesn't end, until the method is present in the functions of this class(self.all_functions)
        is_method: bool = False

        while not(is_method):

            print()

            # write all the possible functions to user, to choose from
            [print(function) for function in self.all_functions]
            print("--------------------------------")

            # get the method as a input from the user
            self.method: str = input("Write a method to use for encryption(possible methods are listed above): ")
            print()

            # assume that, the given method is present in the functions
            is_method = True

            # check, whether the method is actually present, if not ask again
            if self.method not in self.all_functions:
                print("The method is not embedded in this class, so it can not be called. Please give an appropiate Method")
                is_method = False

        return True

    def caesers_cipher(self, shifting_amount: int = 3)  -> str:

        # shift the alphabet according to amount(factually in ceasers cipher is shifting amount 3)
        for _ in range(shifting_amount):
            substitution_letters = self.uppercase_letters[-1] + self.uppercase_letters[:-1]

        # uppercase all the text for better readablity
        self.text = self.text.upper()

        # add all the substituted letters to a dict with corresponding letters in a normal alphabet
        for _ in range(len(substitution_letters)):
            self.letter_mapping[self.uppercase_letters[_]] = substitution_letters[_]

        # also add the case for a space
        self.letter_mapping[" "] = " "

        # create the substituted cipher
        result = ''.join(self.letter_mapping[char] for char in self.text)

        return result
    
    def encrypt(self):

        #*getattr(object, attribute_name, default_value)
        #*  object: The object from which to retrieve the attribute.
        #*  attribute_name: The name of the attribute you want to retrieve (passed as a string).
        #*  default_value (optional): The value returned if the attribute doesn't exist. If not provided and the attribute is missing, an AttributeError will be raised.
        method_function = getattr(self, self.method)

        # use the given method to encrypt the text
        encrypted_text = method_function()

        return encrypted_text

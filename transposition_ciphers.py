
class Transposition_Ciphers():
    
    def __init__(self):

        self.input_text: str = ""
        self.encrypted_final_text: str = ""

    def rail_fence(self, depth):

        # create a empty matrix for the transformation
        matrix = [[[] for _ in range(len(self.input_text))] for _ in range(depth)]

        # fill the matrix with letters according to positions and depth
        level: int = 0
        diff: int = 1
        for letter_index in range(len(self.input_text)):

            matrix[level][letter_index] = self.input_text[letter_index]
            
            if level == depth-1:
                diff = -1
            elif level == 0:
                diff = 1
            level += diff

        # find the letters in each row by row and add together
        for row in matrix:
            for letter in row:
                if letter != []:
                    self.encrypted_final_text += letter.upper()

        return self.encrypted_final_text

bruh = Transposition_Ciphers()
bruh.input_text = "sarparslan"
man = bruh.rail_fence(3)
print(man)
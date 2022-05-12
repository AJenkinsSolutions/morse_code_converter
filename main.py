print("File one __name__ is set to: {}" .format(__name__))

def main():
    #CONSTANTS
    MINOR_SPACE = "SSS"
    MAJOR_SPACE = "SMJ       "
    TWIN_SPACE = "T"

    #MORSE CODE DICTIONARY
    BOOK = {
        '1': '. - - - -',
        '2': '. . - - -',
        '3': '. . . - -',
        '4': '. . . . -',
        '5': '. . . . .',
        '6': '- . . . .',
        '7': '- - . . .',
        '8': '- - - . .',
        '9': '- - - - .',
        '0': '- - - - -',
        '@': '. - - . - .',
        ("A", "a"): ". - ",
        ("B", "b"): "- . . . ",
        ("C", "c"): "- . - .",
        ("D", "d"): "- . .",
        ("E", "e"): ".",
        ("F", "f"): ". . - .",
        ("G", "g"): "- - .",
        ("H", "h"): ". . . .",
        ("I", "i"): ". .",
        ("J", "j"): ". - - -",
        ("K", "k"): "- . -",
        ("L", "l"): ". - . . ",
        ("M", "m"): "- -",
        ("N", "n"): "- .",
        ("O", "o"): "- - -",
        ("P", "p"): ". - - .",
        ("Q", "q"): "- - . -",
        ("R", "r"): ". - .",
        ("S", "s"): ". . .",
        ("T", "t"): "-",
        ("U", "u"): ". . -",
        ("V", "v"): ". . . -",
        ("W", "w"): ". - -",
        ("X", "x"): "- . . -",
        ("Y", "y"): "- . - -",
        ("Z", "z"): "- - . ."
    }

    #FUCNTIONS
    def get_morse(word):
        '''
        Input: String from user
        Compares letters in string to keyt value pairs of a dictionary
        Output: Morse_code equivalent
        '''
        code = []
        previous_letter = None
        for character in word:
            if character == ' ':
                # If there is a space between Words in our string we add a 'Major space' then break from curretn iteration
                code.append(MAJOR_SPACE)
                previous_letter = MAJOR_SPACE
                continue
            for k, v in BOOK.items():
                if character in k:
                    if character == previous_letter:
                        # if character is the same as previous letter add twin space then new letter
                        code.append(TWIN_SPACE)
                        code.append(v)
                        continue
                    # After weve got the correct character we add 'minor space' after
                    if len(code) == 0:
                        # if this is the 1st iteration dont put a space
                        code.append(v)
                        previous_letter = character
                        continue
                    elif previous_letter == MAJOR_SPACE:
                        # If the last letter was a major space dont put a minor space
                        code.append(v)
                        previous_letter = character
                        continue
                    else:
                        # if its not the first iteration. if the previous letter is not the same, if the current letter is not a space, if the preivous letter is not a major space
                        code.append(MINOR_SPACE)
                        code.append(v)
                        previous_letter = character
                        continue
        return code

    #GAME ON CONDITON
    game_on = True

    #User Input and response
    while game_on:
        user_input = str(input('Please provide a String to convert?\n'))
        print(user_input)

        #Converter functionality
        encoded_message = get_morse(user_input)

        #Output Morse Code
        empty_string = ''
        print(empty_string.join(encoded_message))

        # Program Exit
        valid_response = False
        while valid_response == False:

            response = input('Would you like to encode another message?\nType (Y/N)\n').lower()

            if response == 'n':
                game_on = False
                valid_response = True
                print('Goodbye')
                break
            elif response == 'y':
                valid_response = True
                break

            else:
                continue

if __name__ == '__main__':
    main()
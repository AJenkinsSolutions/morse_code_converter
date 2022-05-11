import string

#Alphabet
alpha = string.ascii_lowercase

dit = "."
dahs = "-"
space_min = "SSS"
space_maj = "SMJ       "
twin_space = "T"
book = {
    ("A","a") : ". - ",
    ("B", "b") : "- . . . ",
    ("C", "c") : "- . - ."
    }




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
            #If there is a space between Words in our string we add a 'Major space' then break from curretn iteration
            code.append(space_maj)
            previous_letter = space_maj
            continue
        for k, v in book.items():
            if character in k:
                if character == previous_letter:
                    #if character is the same as previous letter add twin space then new letter
                    code.append(twin_space)
                    code.append(v)
                    continue
                #After weve got the correct character we add 'minor space' after
                if len(code) == 0:
                    #if this is the 1st iteration dont put a space
                    code.append(v)
                    previous_letter = character
                    continue
                elif previous_letter == space_maj:
                    #If the last letter was a major space dont put a minor space
                    code.append(v)
                    previous_letter = character
                    continue
                else:
                    # if its not the first iteration. if the previous letter is not the same, if the current letter is not a space, if the preivous letter is not a major space
                    code.append(space_min)
                    code.append(v)
                    previous_letter = character
                    continue
    return code


code = get_morse('')

print(code)




#TODO:1, User Input and response
# a = input('Please provide a String to convert?')
# print(a)

#TODO:2, Morse Code dictionary




#TODO:3, Converter functionality

#TODO:4, Output Morse Code

#TODO:5,
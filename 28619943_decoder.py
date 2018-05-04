#######################################################################
#                                                                     #
# This file contains the "MorseCodeDecoder" class.                    #
#                                                                     #
# The class contains a Morse code dictionary, "morse_dict" in the     #
# constructor.                                                        #
#                                                                     #
# "__str__" is overwritten to display the structure of "morse_dict"   #
# in a readable format.                                               #
#                                                                     #
# A "decode" function that takes a Morse code sequence as argument is #
# implemented. The function will try to decode the sequence passed to #
# it or generate proper error message.                                #
#                                                                     #
#######################################################################
#                                                                     #
# The program was implemented in python 3.6.4, under PyCharm Edu IDE. #
#                                                                     #
#######################################################################
#                                                                     #
#                               Usage                                 #
# This is a class file that contains the declaration of               #
# "MorseCodeDecoder".                                                 #
#                                                                     #
# This file will be used in 28619943_main.py.                         #
#                                                                     #
#######################################################################
#                                                                     #
# Author: Yezhen Wang                                                 #
# Student ID: 2861 9943                                               #
# Email: ywan0072@student.monash.edu                                  #
# Date Created: April 30, 2018                                        #
# Last Modified: May 4, 2018, 01:30 PM                                #
#                                                                     #
#######################################################################


# declare a python class contains the morse code dictionary and corresponding functions
# where morse code (in 1 and 0s) as the "key", and the
# corresponding English letter, number, or punctuation characters as the "value"
class Decoder:

    # initialize the class with morse code dictionary defined as instance variable
    def __init__(self):
        self.morse_dict = {

            # 26 English letters
            '01': 'A', '1000': 'B', '1010': 'C',
            '100': 'D', '0': 'E', '0010': 'F',
            '110': 'G', '0000': 'H', '00': 'I',
            '0111': 'J', '101': 'K', '0100': 'L',
            '11': 'M', '10': 'N', '111': 'O',
            '0110': 'P', '1101': 'Q', '010': 'R',
            '000': 'S', '1': 'T', '001': 'U',
            '0001': 'V', '011': 'W', '1001': 'X',
            '1011': 'Y', '1100': 'Z',

            # 10 numbers
            '11111': '0', '01111': '1', '00111': '2',
            '00011': '3', '00001': '4', '00000': '5',
            '10000': '6', '11000': '7', '11100': '8',
            '11110': '9',

            # punctuation characters
            '010101': '.', '110011': ',', '001100': '?'
        }

    # overwrite "__str__" function to property print structure of the dictionary
    def __str__(self):

        # initialize output variable with a header
        output = "Structure of morse_dict: \n"

        # loop through "morse_dict" and concatenate keys and values
        for keys, values in self.morse_dict.items():
            output += "Morse Code: " + keys + "\n" + "Value: " + values + "\n"

        return output

    # define decode function, which takes a Morse code sequence as argument
    def decode(self, morse_code_sequence):

        # declare lists for temp handle and result handle
        split_letters = []
        valid_list = []

        # split as words
        split_words = morse_code_sequence.split("***")

        # split as letters, but difference letter and words
        # by adding a space in the end of each word
        for each in split_words:

            # add a space to the end of each word
            each += " "

            # split words into letters
            split_letters += each.split("*")

        # loop through the "split_letter" list, do element check and decoding
        for split_elements in split_letters:

            # check if all the elements are valid Morse code
            if split_elements.strip() not in self.morse_dict:
                return "(Error: Invalid Morse code detected!)"

            # start decoding if all the elements are valid
            # distinguish letter and word here
            else:

                # if the elements is same before and after strip, its a letter
                if split_elements.strip() == split_elements:
                    valid_list.append(self.morse_dict[split_elements])

                # otherwise its a word, add a space in the end
                else:
                    valid_list.append(self.morse_dict[split_elements.strip()])
                    valid_list.append(" ")

        # convert "valid_list" to string and return it
        return ''.join(valid_list)

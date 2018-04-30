#######################################################################
#                                                                     #
# This file contains "CharAnalyze" class.                             #
#                                                                     #
# "__str__" is overwritten to properly display the result of analysis.#
#                                                                     #
# A function called "analyze_characters" is implemented to analyze    #
# the occurrence of each character in the sequence passed.            #
#                                                                     #
#######################################################################
#                                                                     #
# The program was implemented in python 3.6.4, under PyCharm Edu IDE. #
#                                                                     #
#######################################################################
#                                                                     #
#                               Usage                                 #
# This is a class file that contains the declaration of               #
# "CharAnalyze".                                                      #
#                                                                     #
# This file will be used in 28619943_main.py.                         #
#                                                                     #
#######################################################################
#                                                                     #
# Author: Yezhen Wang                                                 #
# Student ID: 2861 9943                                               #
# Email: ywan0072@student.monash.edu                                  #
# Date Created: April 30, 2018                                        #
# Last Modified: April 30, 2018, 05:45 PM                             #
#                                                                     #
#######################################################################


class CharacterAnalyser:

    # initialize the class with occurrence dictionary defined as instance variable
    def __init__(self):
        self.char_occ = {}

    def __str__(self):
        # initialize output variable with a header
        output = "\n\nCharacter occurrence: \n"

        # loop through "char_occ" and concatenate keys and values
        for keys, values in self.char_occ.items():
            output += "Morse Code: " + keys + "\n" + "Value: " + str(values) + "\n"

        return output

    def analyze_characters(self, decoded_sequence):

        # remove spaces and punctuations in the sequence
        decoded_sequence = decoded_sequence.replace(" ", "")
        decoded_sequence = decoded_sequence.replace(",", "")
        decoded_sequence = decoded_sequence.replace(".", "")
        decoded_sequence = decoded_sequence.replace("?", "")

        # check for each character in the string and update "char_occ"
        for each in decoded_sequence:
            if each in self.char_occ:
                self.char_occ[each] += 1
            else:
                self.char_occ[each] = 1

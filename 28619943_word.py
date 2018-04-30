#######################################################################
#                                                                     #
# This file contains "WordAnalyze" class.                             #
#                                                                     #
# "__str__" is overwritten to properly display the result of analysis.#
#                                                                     #
# A function called "analyze_words" is implemented to analyze the     #
# occurrence of each word in the sequence passed.                     #
#                                                                     #
#######################################################################
#                                                                     #
# The program was implemented in python 3.6.4, under PyCharm Edu IDE. #
#                                                                     #
#######################################################################
#                                                                     #
#                               Usage                                 #
# This is a class file that contains the declaration of               #
# "WordAnalyze".                                                      #
#                                                                     #
# This file will be used in 28619943_main.py.                         #
#                                                                     #
#######################################################################
#                                                                     #
# Author: Yezhen Wang                                                 #
# Student ID: 2861 9943                                               #
# Email: ywan0072@student.monash.edu                                  #
# Date Created: April 30, 2018                                        #
# Last Modified: April 30, 2018, 06:11 PM                             #
#                                                                     #
#######################################################################


class WordAnalyser:

    # initialize the class with occurrence dictionary defined as instance variable
    def __init__(self):
        self.word_occ = {}

    def __str__(self):
        # initialize output variable with a header
        output = "\n\nCharacter occurrence: \n"

        # loop through "word_occ" and concatenate keys and values
        for keys, values in self.word_occ.items():
            output += "Morse Code: " + keys + "\n" + "Value: " + str(values) + "\n"

        return output

    def analyze_words(self, decoded_sequence):

        # replace punctuations to spaces
        decoded_sequence = decoded_sequence.replace(",", " ")
        decoded_sequence = decoded_sequence.replace(".", " ")
        decoded_sequence = decoded_sequence.replace("?", " ")

        # split "decoded_sequence" by space, and store the result into a list
        result_list = decoded_sequence.split(" ")

        # loop through the "result_list" and update "word_occ" properly
        for each in result_list:

            # we don't consider empty string as a result
            if each != "":
                if each in self.word_occ:
                    self.word_occ[each] += 1
                else:
                    self.word_occ[each] = 1

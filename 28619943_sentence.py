#######################################################################
#                                                                     #
# This file contains "SentAnalyze" class.                             #
#                                                                     #
# "__str__" is overwritten to properly display the result of analysis.#
#                                                                     #
# A function called "analyze_sentences" is implemented to analyze the #
# occurrence of each sentence in the sequence passed.                 #
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
# Last Modified: May 4, 2018, 01:30 PM                                #
#                                                                     #
#######################################################################


class SentenceAnalyser:

    # initialize the class with occurrence dictionary defined as instance variable
    def __init__(self):
        self.sent_occ = {
            'Clauses': 0,
            'Complete Sentences': 0,
            'Questions': 0
        }

    def __str__(self):
        # initialize output variable with a header
        output = "\nSentence occurrence: \n"

        # loop through "sent_occ" and concatenate keys and values
        for keys, values in self.sent_occ.items():
            output += "Sentence: " + keys + "\n" + "Occurrence: " + str(values) + "\n"

        return output

    def analyse_sentences(self, decoded_sequence):

        # loop through "decoded_sequence" and count for the appearance of each punctuation
        # the update the "sent_occ"
        for each in decoded_sequence:
            if each == ",":
                self.sent_occ["Clauses"] += 1
            elif each == ".":
                self.sent_occ["Complete Sentences"] += 1
            elif each == "?":
                self.sent_occ["Questions"] += 1

#######################################################################
#                                                                     #
# TO BE WROTE                                                         #
#                                                                     #
#######################################################################
#                                                                     #
# The program was implemented in python 3.6.4, under PyCharm Edu IDE. #
#                                                                     #
#######################################################################
#                                                                     #
#                               Usage                                 #
# TO BE WROTE                                                         #
#                                                                     #
#######################################################################
#                                                                     #
# Author: Yezhen Wang                                                 #
# Student ID: 2861 9943                                               #
# Email: ywan0072@student.monash.edu                                  #
# Date Created: April 30, 2018                                        #
# Last Modified: April 30, 2018, 08:05 PM                             #
#                                                                     #
#######################################################################


import re
decoder_class = __import__('28619943_decoder')
char_analyze_class = __import__('28619943_character')
word_analyze_class = __import__('28619943_word')
sent_analyze_class = __import__('28619943_sentence')


if __name__ == "__main__":

    # import classes
    # (import has to be in this way due to files names start with numbers)
    decoder = decoder_class.Decoder()
    char_analyzer = char_analyze_class.CharacterAnalyser()
    word_analyzer = word_analyze_class.WordAnalyser()
    sent_analyzer = sent_analyze_class.SentenceAnalyser()

    # declare a variable that stores a regexp statement will be used to limit user action
    # regexp work as: one or many 0 or 1s, followed by zero or three asterisk
    #                 ending in six 0 or 1s. The pattern appears at least once.
    valid_input = "^([01]+(\*+|([*]{3})+))+[01]{6}$"

    # declare a list to take user inputs
    user_input = []

    # declare a list to store decoded sequences
    decoded_list = []

    # keep taking user input until empty input is detected
    while True:

        # prompt message ask for user input and append input to "user_input" list
        user_input.append(input("Please enter something in Morse code,"
                                "the morse code should be represented by 1 or 0, \n"
                                "singe asterisk (*) is considered as delimiter for characters,"
                                "triple asterisk (***) is \nconsidered as delimiter for words, "
                                "each entry should be ending in a valid punctuation in Morse code. \n"))

        # break the loop if empty input is detected
        if user_input[len(user_input) - 1] == "":
            break

        # check if the last input matches regexp if its not empty
        elif not re.match(valid_input, user_input[len(user_input) - 1]):

            # if the input is not valid, prompt message ask user to re-enter
            while True:

                # stop asking for re-enter if a valid input is received
                if re.match(valid_input, user_input[len(user_input) - 1]):
                    break

                # break the loop if empty input is detected
                elif user_input[len(user_input) - 1] == "":
                    break

                # remove the invalid input first
                # then prompt for a re-enter
                else:
                    user_input = user_input[:-1]
                    user_input.append(input("Invalid input! Please re-enter: \n"))

    # remove the last input (which is the empty input)
    user_input = user_input[:-1]

    # print all user inputs received
    print("\nBelow are the Morse codes you just entered:\n")
    for each in user_input:
        print(each)

        # utilize the same for loop to process decode
        decoded_list.append(decoder.decode(each))

    # print all decoded messages
    print("\n\nBelow are the translated messages:\n")
    for each in decoded_list:
        print(each)

        if each == "(Error: Invalid Morse code detected!)":
            decoded_list.remove(each)

    # remove the error messages stored in the "decoded_list"

    # perform all three analyses the decoded messages
    for each in decoded_list:
        char_analyzer.analyze_characters(each)
        word_analyzer.analyze_words(each)
        sent_analyzer.analyse_sentences(each)

    # print the results of analyses
    print(char_analyzer)
    print(word_analyzer)
    print(sent_analyzer)



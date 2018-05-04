# Morse Code Translator, v2.0
# May 4, 2018

## Assumptions and Limitations:
1.	“28619943_character.py”, “28619943_decoder.py”, “28619943_sentence.py”, and “28619943_word.py” are implemented as classes and are not executable, they are invoked in “28619943_main.py”.
2.	As assignment 1, an improved regular expression “^([01]+(\*?|([*]{3})?))+[01]{6}$” is introduced to limit the user actions.
# Pattern explained:
“digit(s)*(**)digit(s)*(**)…(digits*6)”
(Digits are limited as “1” or “0” s only)

## Instruction for Execution:
System firstly prompt for user input with some instructions, user get to put some Morse codes as input, but the pattern is limited by regular expression. User may enter an empty string as an indication of stop inputting.
After empty string is detected, system will print the Morse codes received, translated messaged, and some proper error message if there's any.
In the end, an option menu will pop out and ask user to choose among the analysis results provided.

# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).
# Examples
#
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"
#
# date of attempt: 6/3/2021
import re

def to_camel_case(text):
    x = re.split("-|_", text)
    for i in range(len(x)-1):
        x[i+1] = x[i+1].capitalize()
    return ''.join(x)

# best practice solution
# def to_camel_case(s):
#     return s[0] + s.title().translate(None, "-_")[1:] if s else s

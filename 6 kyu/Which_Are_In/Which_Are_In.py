# Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2.
#
# #Example 1: a1 = ["arp", "live", "strong"]
#
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
#
# returns ["arp", "live", "strong"]
#
# #Example 2: a1 = ["tarp", "mice", "bull"]
#
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
#
# returns []
# Notes:
#
#     Arrays are written in "general" notation. See "Your Test Cases" for examples in your language.
#
#     In Shell bash a1 and a2 are strings. The return is a string where words are separated by commas.
#
#     Beware: r must be without duplicates.
#     Don't mutate the inputs.
#
# date of attempt: 8/3/2021

def in_array(array1, array2):
    arr = []
    [arr.append(substr) for word in array2 for substr in array1 if substr in word and substr not in arr] # had to separate the lines because of the duplicate check
    arr.sort()
    return arr

# best practice solution
# def in_array(a1, a2):
#     return sorted({sub for sub in a1 if any(sub in s for s in a2)})

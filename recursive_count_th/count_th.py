'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    string = 'th'
    if string not in word:
        return 0
    if (word[0:2] == string):
        return count_th(word[1:]) + 1

    return count_th(word[1:])
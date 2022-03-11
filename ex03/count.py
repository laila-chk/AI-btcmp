import string
import sys

def text_analyzer(txt=None):
    """
    This function counts the number of upper characters, lower characters, punctuation and spaces in a given text.
    """
    if txt is None:
      txt = input("please enter a text so we can analyze it for you! \n")
    if type(txt) is not str:
        print("AssertionError: argument is not a string")
        return
    u = 0
    l = 0
    p = 0
    s = 0
    t = 0
    for cha in txt:
        t += 1
        if cha in string.punctuation:
            p += 1
        elif cha.isupper():
            u += 1
        elif cha.islower():
            l += 1
        elif cha == " ":
            s += 1
    print("The text contains {} character(s):\n- {} upper letter(s) \n- {} lower letter(s) \n- {} punctuation mark(s)\n- {} space(s)".format(t, u, l, p, s))
n = len(sys.argv)
if n >= 3:
    print("Error:too many arguments!")
elif n == 2:
    txt = sys.argv[1]
    text_analyzer(txt)


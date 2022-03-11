import sys
n = len(sys.argv)
x = sys.argv[1]
if n > 2:
    print('AssertionError: more than one argument are provided')
elif not x.isdigit():
    print('AssertionError: argument is not an integer')
elif int(x) == 0:
    print('I\'m Zero.')
elif int(x) % 2 == 1:
    print('I\'m Odd.')
elif int(x) % 2 == 0:
    print('I\'m Even.')

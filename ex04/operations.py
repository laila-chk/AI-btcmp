import sys
n = len(sys.argv)
if n > 3:
    print("AssertionError: too many arguments")
elif n == 2:
    print("AssertionError: too few arguments")
elif n == 3:
    try:
        print("sum: ", int(sys.argv[1])+int(sys.argv[2]))
        print("Difference: ",int(sys.argv[1])-int(sys.argv[2]))
        print("Product: ",int(sys.argv[1])*int(sys.argv[2]))
        if sys.argv[2] == '0':
            print("Quotient: ERROR (division by zero)")
            print("Remainder: ERROR (modulo by zero)")
        else:
            print("Quotient: ",int(sys.argv[1])/int(sys.argv[2]))
            print("Remainder: ",int(sys.argv[1])%int(sys.argv[2]))
    except ValueError:
        print("AssertionError: argument must be an integer!")

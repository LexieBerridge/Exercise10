def add(y, x):
    return y + x


def sub(y, x):
    return y - x


def multiply(y, x):
    return y * x


def divide(y, x):
    return y / x

# this calculation loop will allow you to continue adding further functions and values to a result in an infinite loop
val0 = 0
extensions = 1

while extensions < 2:  # infinite loop
    if val0 == 0:  # if the result of any subsequent calculation = 0 then the code will restart
        functionchoice = input('Please select a function + - / * : ')
        if functionchoice == "+" or "-" or "/" or "*":
            val1 = input('please choose a value: ')
            val2 = input('please choose a second value: ')
            if val1.isdecimal() and val2.isdecimal():
                if functionchoice == "*":
                    print(val1, '*', val2, '=', multiply(int(val1), int(val2)))
                    val3 = (multiply(int(val1), int(val2)))
                    val0 = val0 + val3
                elif functionchoice == "+":
                    print(val1, '+', val2, '=', add(int(val1), int(val2)))
                    val3 = add(int(val1), int(val2))
                    val0 = val0 + val3
                elif functionchoice == "-":
                    print(val1, '-', val2, '=', sub(int(val1), int(val2)))
                    val3 = (sub(int(val1), int(val2)))
                    val0 = val0 + val3
                elif functionchoice == "/":
                    if int(val1) != 0 and int(val2) != 0:
                        print(val1, '-', val2, '=', divide(int(val1), int(val2)))
                        val3 = divide(int(val1), int(val2))
                        val0 = val0 + val3
                    else:
                        print('0 is not a valid input for this function')
                else:
                    print('invalid input please select from options + - / * ')
            else:
                print('invalid input please enter a numeric value')
        else:
            print('invalid input please select from options + - / * ')  # this will print a warning if unlisted functions
    else:
        functionchoice = input('Please select a function + - / * : ')
        if functionchoice == "+" or "-" or "/" or "*":
            val = val0
            val2 = input('please choose a second value: ')
            if val2.isdecimal():
                if functionchoice == "*":
                    print(val0, '*', val2, '=', multiply(int(val0), int(val2)))
                    val3 = (multiply(int(val1), int(val2)))
                    val0 = val0 + val3
                elif functionchoice == "+":
                    print(val0, '+', val2, '=', add(int(val0), int(val2)))
                    val3 = add(int(val0), int(val2))
                    val0 = val0 + val3
                elif functionchoice == "-":
                    print(val0, '-', val2, '=', sub(int(val0), int(val2)))
                    val3 = (sub(int(val0), int(val2)))
                    val0 = val0 + val3
                elif functionchoice == "/":
                    if int(val0) != 0 and int(val2) != 0:
                        print(val0, '-', val2, '=', divide(int(val0), int(val2)))
                        val3 = divide(int(val0), int(val2))
                        val0 = val0 + val3
                    else:
                        print('0 is not a valid input for this function - try again - value stored')
                else:
                    print('invalid input please select from options + - / *  - try again - value stored')
            else:
                print('invalid input please enter a numeric value - try again - value stored')
        else:
            print('invalid input please select from options + - / * - try again - value stored')  # this will print a warning if unlisted functions
else:
    pass

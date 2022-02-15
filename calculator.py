def add(y, x):
    return y + x


def sub(y, x):
    return y - x


def multiply(y, x):
    return y * x


def devide(y, x):
    return y / x


print('for * enter 1')
print('for + enter 2')
print('for - enter 3')
print('for / enter 4')


functionchoice = input('Please select a function 1,2,3,4: ')
if functionchoice.isdecimal():
    if int(functionchoice) == 1 or 2 or 3 or 4:
        val1 = input('please choose a value: ')
        val2 = input('please choose a second value: ')
        if val1.isdecimal() and val2.isdecimal():
            if int(functionchoice) == 1:
                print(val1, '*', val2, '=', multiply(int(val1), int(val2)))
                result = (multiply(int(val1), int(val2)))
            elif int(functionchoice) == 2:
                print(val1, '+', val2, '=', add(int(val1), int(val2)))
                result = add(int(val1), int(val2))
            elif int(functionchoice) == 3:
                print(val1, '-', val2, '=', sub(int(val1), int(val2)))
                result = (sub(int(val1), int(val2)))
            elif int(functionchoice) == 4 and int(val1) != 0 and int(val2) != 0:
                print(val1, '-', val2, '=', devide(int(val1), int(val2)))
                result = devide(int(val1), int(val2))
            elif int(functionchoice) == 4 and int(val1) == 0 or int(val2) == 0:
                print('0 is not a valid input for this function')
        else:
            print('invalid input please enter a numeric value')
    else:
        print('invalid input please select from options 1,2,3,4')  # this will print a warning if unlisted functions
else:
    print('invalid input please enter a numeric value')  # this will print a warning if someone enters a non numeric

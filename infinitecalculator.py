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
exit = "exit"
print("this is a calulator, type 'exit' at any time to stop.")

val1 = input("Please enter a first value: ")
if val1 != exit:
    if val1.isdecimal():
        while val0 != "nonsense":
                functionchoice = input('please enter a functionchoice +, -, /, * :')
                if functionchoice == "exit":
                    print("thankyou goodbye")
                    break
                elif functionchoice == "+" or "-" or "/" or "*":
                        val2 = input('please choose a second value: ')
                        if val2 == "exit":
                            print('thankyou goodbye')
                            break
                        elif val2.isdecimal():
                                if functionchoice == "*":
                                    print(val1, '*', val2, '=', multiply(int(val1), int(val2)))
                                    val3 = (multiply(int(val1), int(val2)))
                                    val1 = 0 + val3
                                elif functionchoice == "+":
                                    print(val1, '+', val2, '=', add(int(val1), int(val2)))
                                    val3 = add(int(val1), int(val2))
                                    val1 = 0 + val3
                                elif functionchoice == "-":
                                    print(val1, '-', val2, '=', sub(int(val1), int(val2)))
                                    val3 = (sub(int(val1), int(val2)))
                                    val1 = 0 + val3
                                elif functionchoice == "/":
                                    if int(val1) != 0 and int(val2) != 0:
                                        print(val1, '-', val2, '=', divide(int(val1), int(val2)))
                                        val3 = divide(int(val1), int(val2))
                                        val1 = 0 + val3
                                    else:
                                        print('0 is not a valid input for this function')
                                else:
                                    print('invalid input please select from options + - / * ')
                        else:
                            print("oops, please enter a number or 'exit' to stop")
                else:
                    print('invalid input please select from options + - / * ')
        else:
            pass
    else:
        print("oops, please enter a number or 'exit' to stop")
else:
    print("thankyou, goodbye")



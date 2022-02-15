import getpass
# this code only works when ran in 'Emulate terminal in output console'
# this is selected in 'Run Configurations' under 'Execution'

correctpin = "1234"   # pin represented as string
maximumattempts = 3   # cust pin will lock after 3 invalid attempts
attempts = 1   # customers first attempt will be considered 1


while attempts < maximumattempts:
    pin = getpass.getpass(prompt='Please enter your pin: ')  # this hides customer pin as they enter it
    pin = pin.strip()  # pin denoted as .stip() so input is considered string should the cust enter a space
    if pin in correctpin:
        print('pin accepted')
        break
    if pin not in correctpin:
        print('incorrect pin, try again')
        attempts = attempts + 1   # invalid attempt customer has maximumattempts -1 attempt
        if pin in correctpin:
            print('Pin accepted')
            break
    if attempts == maximumattempts:
        pin = getpass.getpass(prompt='Please enter your pin: ')
        pin = pin.strip()
        if pin in correctpin:
            print('pin accepted')
        else:
            print('your pin has been locked. you have exceeded your maximum attempts')
            attempts = attempts + 1
else:
    pass

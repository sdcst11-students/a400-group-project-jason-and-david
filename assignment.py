#!python3
# Volume Calculator
# Feel free to rename your variables

#addition, subtraction, multiplication, division, area, volume, square root, surface area.

def title(symbol = '='):
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author: David
    # Modified: David
    # title
    output = f"{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}\n{symbol} Calculator {symbol}\n{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}"
    return output

#def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author: Jason
    # Modified:
    output = print("---------------------------------------------------------------------------------------------")
    print("| print out one of the calculations you choose to use =                                     |")
    print("| addition, subtraction, multiplication, division, area, volume, square root, surface area. |")
    print("---------------------------------------------------------------------------------------------")
    return output
    



#def main():
    """
    main block of code that will run your program and control program flow
    You will need to include a while loop to keep repeating the commands until
    the user chooses to exit
    """
    decision = input("If you want to exit enter 'Exit' and if you want to stay enter 'Continue'")
    if decision == 'Continue' or decision == "continue":
        title()
        while True:
        # keep giving options to choose menu options until they choose to exit
            pass
    elif decision == 'Exit' or decision == 'exit':
        print("==============\n= Good Bye! =\n==============")

if __name__ == "__main__":
    print(title())
    print(main())


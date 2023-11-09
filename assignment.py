#!python3
# Volume Calculator
# Feel free to rename your variables

#addition, subtraction, multiplication, division, area, volume, square root, surface area.
import math

def title(symbol = '='):
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author: David
    # Modified: David
    # title
    output = f"{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}\n{symbol} Calculator {symbol}\n{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}"
    return output

def instructions():
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
    

def main():
    """
    main block of code that will run your program and control program flow
    You will need to include a while loop to keep repeating the commands until
    the user chooses to exit
    """
    type_of_calc = (input("Choose what you want to calculate: "))
    if type_of_calc == 'Addition' or type_of_calc == 'addition':
        add_a = int(input('Enter a number: '))
        add_b = int(input('Enter a number to add to the first number: '))
        sum = add_a + add_b
        print(f"The sum of {add_a} and {add_b} is {sum}")
    elif type_of_calc == 'Subtraction' or type_of_calc == 'subtraction':
        sub_a = int(input('Enter a number: '))
        sub_b = int(input('Enter a number to subtract from the previous number: '))
        diff = sub_a - sub_b
        print(f"The difference of {sub_a} and {sub_b} is {diff}")
    elif type_of_calc == 'Multiplication' or type_of_calc == 'multiplication':
        mult_a = int(input('Enter a number: '))
        mult_b = int(input('Enter a number to multiply the first number by: '))
        prod = mult_a * mult_b
        print(f"The product of {mult_a} and {mult_b} is {prod}")

    decision = input("If you want to exit enter 'Exit' and if you want to stay enter 'Continue'")
    if decision == 'Continue' or decision == "continue":
        print(title())
        while True:
        # keep giving options to choose menu options until they choose to exit
            pass
    elif decision == 'Exit' or decision == 'exit':
        print("==============\n= Good Bye! =\n==============")

if __name__ == "__main__":
    print(title())
    print(instructions())
    print(main())


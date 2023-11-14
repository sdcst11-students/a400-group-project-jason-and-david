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
    print("---------------------------------------------------------------------------------------------")
    print("| print out one of the calculations you choose to use =                                     |")
    print("| addition, subtraction, multiplication, division, area, volume, square root, surface area. |")
    print("---------------------------------------------------------------------------------------------")
    

def main():
    """
    main block of code that will run your program and control program flow
    You will need to include a while loop to keep repeating the commands until
    the user chooses to exit
    """
    type_of_calc = (input("Choose what you want to calculate: "))
    if type_of_calc == 'Addition' or type_of_calc == 'addition':
        add_a = float(input('Enter a number: '))
        add_b = float(input('Enter a number to add to the first number: '))
        sum = add_a + add_b
        print(f"The sum of {add_a} and {add_b} is {sum}.")
    elif type_of_calc == 'Subtraction' or type_of_calc == 'subtraction':
        sub_a = float(input('Enter a number: '))
        sub_b = float(input('Enter a number to subtract from the previous number: '))
        diff = sub_a - sub_b
        print(f"The difference of {sub_a} and {sub_b} is {diff}.")
    elif type_of_calc == 'Multiplication' or type_of_calc == 'multiplication':
        mult_a = float(input('Enter a number: '))
        mult_b = float(input('Enter a number to multiply the first number by: '))
        prod = mult_a * mult_b
        print(f"The product of {mult_a} and {mult_b} is {prod}.")
    elif type_of_calc == 'Division' or type_of_calc == 'division':
        div_a = float(input('Enter a number: '))
        div_b = float(input('Enter a number to multiply the first number by: '))
        quot = div_a / div_b
        quot(round(quot))
        print(f"The quotient of {div_a} and {div_b} is {quot}.")
    elif type_of_calc == 'Area' or type_of_calc == 'area':
        area_a = float(input('Enter the value of the first side: '))
        area_b = float(input('Enter the value of the second side: '))
        area = area_a * area_b
        print(f"The area of {area_a} and {area_b} is {area}.")
    elif type_of_calc == 'Volume' or type_of_calc == 'volume':
        vol_a = float(input('Enter the value of the height: '))
        vol_b = float(input('Enter the value of the width: '))
        vol_c = float(input('Enter the value of the length: '))
        vol = vol_a * vol_b * vol_c
        print(f"The volume of {vol_a}, {vol_b}, and {vol_c} is {vol}.")
    elif type_of_calc == 'Surface Area' or type_of_calc == 'Surface area' or type_of_calc == 'surface area':
        sa = float(input('Enter the length value of the cube: '))
        ans = 6*(sa**2)
        print(f"The surface area of {sa} is {ans}.")
    elif type_of_calc == 'Square root' or type_of_calc == 'square root':
	    sqrt_num = float(input('Enter a number to square root: '))
	    sqrt = math.sqrt(sqrt_num)
	    print(f'The square root of {sqrt_num} is {sqrt}')
    decision = input("If you want to exit enter 'Exit' and if you want to stay enter 'Continue' ")
    if decision == 'Continue' or decision == "continue":
        while True:
        # keep giving options to choose menu options until they choose to exit
            print(title())
            print(instructions())
            print(main())
            pass
    elif decision == 'Exit' or decision == 'exit':
        print("==============\n= Good Bye! =\n==============")

if __name__ == "__main__":
    print(title())
    print(instructions())
    print(main())


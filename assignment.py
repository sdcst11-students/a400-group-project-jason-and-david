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
    print("| Type one of the following calculations =                                                  |")
    print("| addition, subtraction, multiplication, division, area, volume, square root, surface area. |")
    print("---------------------------------------------------------------------------------------------")
    

def main():
    """
    main block of code that will run your program and control program flow
    You will need to include a while loop to keep repeating the commands until
    the user chooses to exit
    """
    type_of_calc = (input("Choose what you want to calculate: "))
    if type_of_calc.lower() == 'addition':
        add_a = float(input('Enter a number: '))
        add_b = float(input('Enter a number to add to the first number: '))
        sum = add_a + add_b
        sum = round(sum,2)
        print(f"The sum of {add_a} and {add_b} is {sum}.")
    elif type_of_calc.lower() == 'subtraction':
        sub_a = float(input('Enter a number: '))
        sub_b = float(input('Enter a number to subtract from the previous number: '))
        diff = sub_a - sub_b
        diff = round(diff,2)
        print(f"The difference of {sub_a} and {sub_b} is {diff}.")
    elif type_of_calc.lower() == 'multiplication':
        mult_a = float(input('Enter a number: '))
        mult_b = float(input('Enter a number to multiply the first number by: '))
        prod = mult_a * mult_b
        prod = round(prod,2)
        print(f"The product of {mult_a} and {mult_b} is {prod}.")
    elif type_of_calc.lower() == 'division':
        div_a = float(input('Enter a number: '))
        div_b = float(input('Enter a number to multiply the first number by: '))
        quot = div_a / div_b
        quot = round(quot)
        print(f"The quotient of {div_a} and {div_b} is {quot}.")
    elif type_of_calc.lower() == 'area':
        area_a = float(input('Enter the value of the first side: '))
        area_b = float(input('Enter the value of the second side: '))
        area = area_a * area_b
        area = round(area,2)
        print(f"The area of {area_a} and {area_b} is {area}.")
    elif type_of_calc.lower() == 'volume':
        vol_a = float(input('Enter the value of the height: '))
        vol_b = float(input('Enter the value of the width: '))
        vol_c = float(input('Enter the value of the length: '))
        vol = vol_a * vol_b * vol_c
        vol = round(vol,2)
        print(f"The volume of {vol_a}, {vol_b}, and {vol_c} is {vol}.")
    elif type_of_calc.lower() == 'surface area':
        sa = float(input('Enter the length value of the cube: '))
        ans = 6*(sa**2)
        ans = round(ans,2)
        print(f"The surface area of {sa} is {ans}.")
    elif type_of_calc.lower() == 'square root':
	    sqrt_num = float(input('Enter a number to square root: '))
	    sqrt = math.sqrt(sqrt_num)
        #sqrt = round(sqrt,2)
	    print(f'The square root of {sqrt_num} is {sqrt}')
    else:
        while True: 
            print('\nInvalid Input\nPlease try again\n')
            print(title())
            instructions()
            main()
    # keep giving options to choose menu options until they choose to exit
    while True:
        decision = input("If you want to exit enter 'Exit' and if you want to stay enter 'Continue' ")
        if decision.lower() == 'continue':
                print(title())
                instructions()
                main()
        elif decision.lower() == 'exit':
            print("==============\n= Good Bye! =\n==============")
            break
        else: 
            print('Invalid input, please try again')
            

if __name__ == "__main__":
    print(title())
    instructions()
    main()
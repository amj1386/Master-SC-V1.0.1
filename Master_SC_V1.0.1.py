import math
import mpmath
import time
import datetime
from persiantools.jdatetime import JalaliDate
from pytz import timezone



def welcome():
    print('''
       (⌐■_■)
       welcome to scientific Calculator / virtual machin for calulations V1.0.1(CMD)
       ISW Corporation™. all rights reserved 2022.
       New Version (1.2.0) Is Coming...''')
    x_if = JalaliDate.today()
    y_els = datetime.datetime.now()
    t_tz = str(datetime.datetime.now(timezone("Asia/Tehran")))
    t_tz = t_tz.replace("+04:30", "")
    now = str(datetime.datetime.now())
    now2_els = datetime.datetime.now()
    now_if = datetime.datetime.now()

    if now == t_tz:
        print(f'       IRI | {now_if.strftime("%A")} | {now_if.strftime("%X")} | {x_if} (SH)\n')
    else:
        print(f'       ITN | {now2_els.strftime("%A")} | {now2_els.strftime("%X")} | {y_els.strftime("%x")} (AD)\n')
        
# ITN in up is same International

def sections():
    user_selection = input('''which section do you want?
 | cc for classic calculations
 | bc for BMI calculation
 | dc for date calculation
 | uc for unit converter
  ''')
    if user_selection.lower() == "cc":
        c_calculator()
    elif user_selection.lower() == "bc":
        b_calculator()
    elif user_selection.lower() == "dc":
        d_calculator()
    elif user_selection.lower() == "uc":
        u_converter()
    else:
        print("was not correct something that enter, enter again.")
        sections()

def again():
    calc_again = input('''
Do you want to calculate again? Please type:
  YS for go to sections of calculator
  YCC for go to classic calculator
  YBC for go to BMI calculator
  YDC for go to date calculator
  YUC for go to units converter
  N for exit
    ''')
    if calc_again.upper() == 'YS':
        sections()
    elif calc_again.upper() == 'YCC':
        c_calculator()
    elif calc_again.upper() == 'YBC':
        b_calculator()
    elif calc_again.upper() == 'YDC':
        d_calculator()
    elif calc_again.upper() == 'YUC':
        u_converter()
    elif calc_again.upper() == 'N':
        print('''
------------------
| See you later. |
------------------
''')
        time.sleep(3)
    else:
        print("was not correct something that enter, enter again.")
        again()


def c_calculator():
    try:
        operation = input('''
    Please type One of the allowed operators below:
    --------------------------------------------------
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ** for power
    % for To see the remainder of the division
    abs for absolute of the number
    sq for square of the number
    ! for factorial of the natural number
    gcd for Greatest Common Divisor of two integer numbers
    sin for returns the sine of the number
    cos for returns the cosine of a number
    tan for returns the tangent of the number
    cot for returns the cotangent of the number
    --------------------------------------------------
        ''')
        if operation == '+':
            number_1 = float(input("Enter your first number: "))
            number_2 = float(input("Enter your second number: "))
            output_number = number_1 + number_2
            print( "{} + {} = {}".format(number_1, number_2, output_number))
        elif operation == '-':
            number_1 = float(input("Enter your first number: "))
            number_2 = float(input("Enter your second number: "))
            output_number = number_1 - number_2
            print( "{} - {} = {}".format(number_1, number_2, output_number))
        elif operation == '*':
            number_1 = float(input("Enter your first number: "))
            number_2 = float(input("Enter your second number: "))
            output_number = number_1 * number_2
            print( "{} * {} = {}".format(number_1, number_2, output_number))
        elif operation == '/':
            number_1 = float(input("Enter your first number: "))
            number_2 = float(input("Enter your second number: "))
            output_number = number_1 / number_2
            print( "{} / {} = {}".format(number_1, number_2, output_number))
        elif operation == '**':
            number_1 = float(input("Enter your first number: "))
            number_2 = float(input("Enter your second number: "))
            output_number = number_1 ** number_2
            print("{} ** {} = {}".format(number_1, number_2, output_number))
        elif operation == '%':
            number_1 = float(input("Enter your first number: "))
            number_2 = float(input("Enter your second number: "))
            output_number = number_1 % number_2
            print("{} % {} = {}".format(number_1, number_2, output_number))
        elif operation.lower() == 'abs':
            number_1 = float(input("Enter your number: "))
            output_number1 = abs(number_1)
            print(f"absolute of number({number_1}) is {output_number1}")
        elif operation.lower() == 'sq':
            number_1 = float(input("Enter your number: "))
            output_number1 = math.sqrt(number_1)
            print(f"square of number({number_1}) is {output_number1}")
        elif operation == '!':
            number_1 = int(input("Enter only your natural number: "))
            output_number1 = math.factorial(number_1)
            print(f"factorial of number({number_1}) is {output_number1}")
        elif operation.lower() == 'gcd':
            number_1 = int(input("Enter your first integer number only: "))
            number_2 = int(input("Enter your second integer number only: "))
            output_number = math.gcd(number_1, number_2)
            print(f"Greatest Common Divisor of two numbers({number_1} and {number_2}) is {output_number}")
        elif operation.lower() == 'sin':
            number_1 = float(input("Enter your number(to degree): "))
            tmp = math.radians(number_1)
            output_number1 = math.sin(tmp)
            print(f"sine of number({number_1}) is {output_number1}")
        elif operation.lower() == 'cos':
            number_1 = float(input("Enter your number(to degree): "))
            tmp = math.radians(number_1)
            output_number1 = math.cos(tmp)
            print(f"cosine of number({number_1}) is {output_number1}")
        elif operation.lower() == 'tan':
            number_1 = float(input("Enter your number(to degree): "))
            if number_1 == 45:
                number_1 = math.ceil(number_1)
            tmp = math.radians(number_1)
            output_number1 = math.tan(tmp)
            print(f"tagent of number({number_1}) is {output_number1}")
        elif operation.lower() == 'cot':
            number_1 = float(input("Enter your number(to degree): "))
            tmp = math.radians(number_1)
            output_number1 = mpmath.cot(tmp)
            print(f"cotangent of number({number_1}) is {output_number1}")
        else:
            print('You have not typed a valid operator, please enter again')
            c_calculator()
        again()
    except:
        print('''
        ||| format of something that enter not correct, enter again. |||
        ''')
        c_calculator()

def b_calculator():
    try:
        mass_entered = float(input("please enter your mass to kg: "))
        hight_entered = float(input("please enter your height to meter: "))
        h_s = hight_entered**2
        answer = mass_entered/h_s
        guide_answer = ("\n● if your bmi is between 10.3 to 18.4, you are thin.\n● if it's between 18.5 to 24.9, your bmi is normall.\n● if it's between 25.0 to 29.4, you are overmass. and in the range of 30.0 to 71.4, your obesity is dangerous and even deadly.\n")
        print(f"\n{answer}\n")
        print(guide_answer)
        again()
    except:
        print('''
        ||| format of something that enter not correct, enter again. |||
        ''')
        b_calculator()

def d_calculator():
    operation = input('''
Please type One of the allowed operators below:
--------------------------------------------------
  bir_ad for that you see your birthday to ad
  bir_sh for that you see your birthday to sh
--------------------------------------------------
''')
    try:
        if operation.lower() == "bir_ad":
            def converter_shtoad(day, month, year):
                if month > 10 or day > 10 and month == 10:
                    birthday = year + 622
                else:
                    birthday = year + 621
                    print(f"your year of birthday to AD is {birthday}")
            converter_shtoad(int(input("enter day: ")), int(input("enter month: ")), int(input("enter year: ")))
        if operation.lower() == "bir_sh":
            def converter_adtosh(day, month, year):
                if month > 10 or day > 10 and month == 10:
                    birthday = year - 622
                else:
                    birthday = year - 621
                print(f"your year of birthday to SH is {birthday}")
            converter_adtosh(int(input("enter day: ")), int(input("enter month: ")), int(input("enter year: ")))
        else:
            print('You have not typed a valid operator, please enter again')
            d_calculator()
        again()
    except:
        print('''
        ||| format of something that enter not correct, enter again. |||
        ''')
        d_calculator()

def u_converter():
    operation = input('''
Please type One of the allowed operators below:
--------------------------------------------------
    ang for convert units of angle
    tmr for convert units of temperature
--------------------------------------------------
    ''')
    try:
        if operation.lower().replace(" ", "") == "ang":
            operation2 = input('''
    (radian to degree and gradian) type RDG
    (degree to radian and gradian) type DRG
    (gradian to radian and degree) type GRD
            ''')
            if operation2.upper() == "RDG":
                number_1 = float(input("please enter radian to number: "))
                output_d = math.degrees(number_1)
                output_g = output_d / 0.9
                print(f"your temperature(radian) to degree is {output_d} and to gradin is {output_g}")
            elif operation2.upper() == "DRG":
                number_1 = float(input("please enter degree to number: "))
                output_r = math.radians(number_1)
                output_g = number_1 / 0.9
                print(f"your temperature(degree) to radian is {output_r} and to gradin is {output_g}")
            elif operation2.upper() == "GRD":
                number_1 = float(input("please enter gradian to number: "))
                output_d = number_1 * 0.9
                output_r = math.radians(output_d)
                print(f"your temperature(gradian) to radian is {output_r} and to degree is {output_d}")
            else:
                print('You have not typed a valid operator, please enter again')
                u_converter()
            again()
        if operation.lower().replace(" ", "") == "tmr":
            operation2 = input('''
            (Celsius to Kelvin and Fahrenheit) type CKF
            (Kelvin to Fahrenheit and Celsius) type KFC
            (Fahrenheit to Celsius and Kelvin) type FCK
            ''')
            if operation2.upper() == "CKF":
                number_1 = float(input("please enter Celsius to number: "))
                output_k = number_1 + 273.15
                output_f = (number_1 * 1.8) + 32
                print(f"your temperature({number_1} Celsius) to Kelvin is {output_k} and to Fahrenheit is {output_f}")
            elif operation2.upper() == "KFC":
                number_1 = float(input("please enter Kelvin to number: "))
                output_c = number_1 - 273.15
                output_f = (output_c * 1.8) + 32
                print(f"your temperature({number_1} Kelvin) to Fahrenheit is {output_f} and to Celsius is {output_c}")
            elif operation2.upper() == "FCK":
                number_1 = float(input("please enter Fahrenheit to number: "))
                output_c = (number_1 - 32) / 1.8
                output_k = output_c + 273.15
                print(f"your temperature({number_1} Fahrenheit) to Celsius is {output_c} and to Kelvin is {output_k}")
            else:
                print('You have not typed a valid operator, please enter again')
                u_converter()
            again()
        else:
            print('You have not typed a valid operator, please enter again')
            u_converter()
    except:
        print('''
        ||| format of something that enter not correct, enter again. |||
        ''')
        u_converter()

welcome()
sections()

# Name Program: Master Scientific Calculator V1.0.1
# Status of UI: with no UI
# Version: 1.0.1(CMD)
# Publisher: ISW

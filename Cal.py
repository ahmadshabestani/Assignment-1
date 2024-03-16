import math
oprator = input("select  +  -  *  /  sin cos tan sqrt cot  factorial:")
if oprator == "+" or oprator == "-" or oprator == "*" or oprator == "/":
    number1 = float(input("Enter your Number : "))
    number2 = float(input("Enter your Number : "))
if oprator == "sin" or oprator == "cos" or oprator == "tan" or oprator == "cot" or oprator == "factorial" or oprator == "sqrt":
    number1 = float(input("Enter your Number : "))
if oprator == "+":
    result = number1 + number2
if oprator == "-":
    result = number1 - number2
if oprator == "*":
    result = number1 * number2
if oprator == "/":
    if number2 == 0:
        result = "Not Number"
    else:
        result = number1 / number2
if oprator == "sin":
    result = math.sin(number1)
if oprator == "cos":
    result = math.cos(number1)
if oprator == "tan":
    result = math.tan(number1)
if oprator == "sqrt ":
    result = math.sqrt(number1)
if oprator == "cot":
    angle_rad = math.radians(number1)
    result = 1 / math.tan(angle_rad)
if oprator == "factorial":
    result = math.factorial(number1)
print(result)
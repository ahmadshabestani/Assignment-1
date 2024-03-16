number1 = int(input("Enter your Number 1 :"))
number2 = int(input("Enter your Number 2 :"))
number3 = int(input("Enter your Number 3 :"))


if number1 < (number2 + number3) and number2 < (number1 + number3) and number3 < (number1 + number2):
    print("you can create triangle")
else:
    print("you cant")
# name1 = input("Enter your Name : ")
# family1 = input("Enter your  family : ")
number1 = float(input("Enter your Number : "))
# name2 = input("Enter your Name : ")
# family2 = input("Enter your  family : ")
number2 = float(input("Enter your Number : "))
# name3 = input("Enter your Name : ")
# family3 = input("Enter your  family : ")
number3 = float(input("Enter your Number : "))

avrage = (number1 + number2 + number3) / 3

if avrage >= 17:
    print("Great")
elif avrage < 17 and avrage >= 12:
    print("Normal")
elif avrage < 12:
    print("Fail")

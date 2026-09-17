#positive,negative or zero
'''num = int(input("Enter your Number"))
if num > 0:
    print("positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")'''

#even or odd
'''num = int(input("Enter your Number:"))
if num % 2 == 0:
    print("Even")
elif num % 2 != 0:
    print("Odd")
else:
    print("Zero")'''

#largest number
'''a = int(input("Enter your a value:"))
b = int(input("Enter your b value:"))
if a > b:
    print("a is larger")
elif a == b:
    print("both are equal")
else:
    print("b is larger")'''

#college admission
'''marks = int(input("Enter marks: "))
entrance = input("Did you pass entrance exam(yes,no)")
if marks >= 60 and entrance == 'yes':
    print("Eligible for admission")
elif marks >= 60 and entrance == 'no':
    print("Not eligible for admission")
elif marks <= 60 and entrance == 'yes':
    print("Not eligible for admission")
else: 
    print("you are eligible")'''



#Login system
'''username = input("Enter the username")
password = input("Enter your password")

if username == "sai" and password == "password123":
    print("Login successful")
else:
    print("Login Failed. Please try again!")'''

#driving license
'''age = int(input("Enter your age:"))
license_valid = input("yes/no:")
if age >= 18:
    if license_valid == "yes":
        print("You can drive")
    else:
        print("Valid license required")
else:
    print("get way kid!")'''

#movie tickets
'''age = int(input("enter your age:"))
if age < 5:
    print("Free for you liitle one")
elif age in range(5,12):
    print("Your ticket cost is 100")
elif age in range(13,59):
    print("Your ticket is 200")
else:
    print("Your ticket is 120 oldman")'''


#leap year
'''year = int(input("Enter the year:"))
if year % 400 == 0:
    print("It is a leap year")
elif year % 100 == 0:
    print("It is not a leap year")
elif year % 4 == 0:
    print("It is a leap year")
else:
    print("It is not a leap year")'''


#employee management system
performance = int(input("Enter the percentage:"))
experience = int(input("Enter the Experience"))
if performance > 90 and experience > 5:
    print("you got 20% hike")
elif performance > 90 and experience < 5:
    print("Sorry buddy due to less experience you will get only 10% hike")
elif performance > 80:
    print("you got 10% hike buddy")
else:
    print("you guys get only 5% hike")
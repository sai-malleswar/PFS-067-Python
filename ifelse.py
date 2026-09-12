'''age = int(input())
if age >= 21:
    print("permiited")
else:
    print("not permitted")

marks = int(input())
if marks >= 90:
    print("O")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
else:
    print("F")


age = int(input())
has_id = True
if age >= 21:
    print("satisfied")
    if has_id:
        print("lopaliki pondi")


card_valid = True
correct_pin = 1324
balance = 10000000

if card_valid:
    print("your card is valid")

    pin = int(input("Enter your PIN:"))
    if pin == correct_pin:
        print("You have entered the correct pin.")
        if pin != correct_pin:
            print("You have entered the wrong pin")
    amount = int(input("Enter the amount you want to withdraw:"))
    if amount <= balance:
        print("you have sufficient amount")
    else:
        print("not sufficient amount")
    balance = balance - amount
    print("collect you money")
    print("remaining balance is:",balance)
else:
    print("card is not valid")
print("Thank you for using our services")'''


product_available = True or False
correct_username = "sai"
correct_password = "1234"

if product_available:
    print("Product is available")

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login successful")

        payment = input("Was payment completed? (yes/no): ")

        if payment == "yes":
            print("Payment successful")
            print("Order confirmed!")

        else:
            print("Payment failed")
            print("Order not confirmed")

    else:
        print("Invalid username or password")

else:
    print("Product is out of stock")
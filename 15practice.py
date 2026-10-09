#Palindrome
'''num = int(input("Enter a num: "))
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
if original == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")'''


#factorial:
'''num = int(input("Enter your number: "))
factorial = 1
while num > 0:
    factorial  *= num
    num -= 1
print(factorial)''' 

#fibonnaci series
'''n= int(input("Enter a numbet: "))
a = 0
b = 1
for i in range(n):
    print(a,end=" ")
    a,b = b,a + b'''


#finding duplicate numbers in the list
num = [1,2,3,4,5,5,3,6,7,8,9,1,2,4]
for i in range(len(num)):
    for j in range(i + 1, len(num)):
        if num[i] == num[j]:
            print(num[i])


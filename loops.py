#1)by using index
#for i in range(0, 10):
 #   print(i)

#nums = [10,20,30,40,50]
#for i in range(0,5):
 #   print(i,nums[i])

#by using value
#nums = [10,20,30,40,50]
#for num in nums:
#    print(num)


#While loop
#i = 0
#while i <= 5:
#    print(i)
#    i += 1


#print even numbers from 1 to10
#i = 0
#for i in range(0,11):
#    if i % 2 == 0:
#        print(i)


#print nos from 10 to 1
#i =10
#while i >= 1:
#    print(i)
#    i -= 1

#total= 0
#n = int(input())
#for i in range(1,n+1):
#    total += i
#print(total)

#multiplication table
#num = int(input("Enter your no:"))
#for i in range(1,11):
#    print(num * i)


#finding largest no in array without max()
nums = [10,20,30,40,50]
largest = 0
for num in nums:
    if num > largest:
        largest = num
print(largest)


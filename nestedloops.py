#for i in range(0,2):
 #   for j in range(0,10):
  #      print(i,j)

#star patterns
#for i in range(1,6):
 #   for j in range(i):
  #      print(" * ",end="")
   # print()
#1st iter = i = 1,j=(0,1) j =0
#2nd iter = i =2 ,j=(0,2)
#3rd iter = i = 3 ,j(0,3)=0,1,2
#4th iter = i =4,j(0,4)=0,1,2,3
#5th iter = i=5,j(0,5) = 0,1,2,3,4


#decreasing pattern
#for i in range(5,0,-1):
#    for j in range(i):
#        print(" * ",end = " ")
#    print()

#complete pattern
#for i in range(1,6):
#    for j in range(i):
#        print("*",end = " ")
#    print()
#for i in range(5,0,-1):
#    for j in range(i):
#        print("*",end = " ")
#    print()

#square pattern
#for i in range(5):
#    for j in range(5):
#        print("*",end = " ")
#    print()


#rectangle pattern
#for i in range(4):
#   for j in range(8):
#       print("*",end = " ")
#   print()

#Spaced pattern
#n = 5
#for i in range(1,n+1):
#    for j in range(n-i):
#        print(" ",end="")
#    for j in range(i):
#        print("*",end = "")
#    print()

#1st iter = i(1,6)->1,2,3,4,5-> i =1
#j in range(0,4) 0123

#pyramid pattern
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print("-",end="")
    for j in range(2*i - 1):
        print("*",end="")
    print()
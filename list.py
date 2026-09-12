#list concatenation

#a = [10,20]
#b = [30,40]
#result = a+b
#print(result)

#list repetition
'''a=["sai","malleswar"]
print(a * 3)'''

#Built in functions
#1.maximum - max() - it returns element in the list
'''a=[10,20,20,30,40]
print(max(a))

#2.length - len() - it returns no.of elements in the list
b=[10,20,30,40,50,60,70,80,90,100]
print(len(b))

#3.sum()- add elements in the list
c=[100,200,28,9,2005]
print(sum(c))

#4.sorted - sorted() - it is used to sort the list if it is unsorted
d=[30,70,111,2005,28,5]
print(sorted(d))'''


#List methods
#1.Append() - adding element to the end
a=[10,20]
a.append(30)
print(a)

#2.extend - adds more than two values
nums = [10,20,30]
nums.extend([40,50,60])
print(nums)

#3.insert - adding a element at a particular position


#remove - removes the first matching value
b=[10,20,30,20]
b.remove(20)
print(b)
b=[10,30,20]
b.remove(20)
print(b)

#pop - it removes an element from the last


#index - returns the index of first matching value
c=[10,20,30,20]
print(c.index(20))

#count - counts no of occurrences
print(c.count(20))

#sort() - sort the existing list in place
d=[10,20,30,40,90,79,80,60]
d.sort()
print(d)

#reverse - reverse the list
e=["sai","malleswar"]
e.reverse()
print(e)
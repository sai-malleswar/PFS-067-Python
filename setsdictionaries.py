'''name = {10,20,20,30,50,60,50}
print(name)

nums = set()
print(type(nums))

nums = {10,20,30,40}
nums.add(40)
print(nums)'''

#Set Operations
#union,intersection,difference,symmetric difference

#union - combie all the elements from both sets,without dupicates (|)
'''A = {10,20,30}
B = {30,40,50}
print(A|B)

#union using method()
print(B.union(A))

#intersection - classifies common elements
print(A&B)
#using method()
print(A.intersection(B))

#difference - elements that exists in the first set but not in the second set.denoted by (-)
print(A-B)
print(B-A)

#symmetric difference - elements that are in either sets but not in both. denoted by(^)
print(A^B)'''

#set main methods
'''nums = {10,20,30,40}
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
nums.add(50)
print(nums)
#if we use sorted on the set it will print the result in a list because a set is an unordered collection of data
nums.update({60,70,80})
nums.update([100,110])
print(nums)
nums.remove(110)
nums.pop()
nums.discard(100)
nums.clear()
print(nums)'''


#dictionary - collection of key - value pairs
'''student = {
    "name" : "sai",
    "age" : 20,
    "course" : "pfs",
    "fee" : 40000
}
print(student["name"])
print(student["age"])
print(student["course"])
print(student.get("fee"))

#adding a new key
#dict_name["new_key"] = "value"
student["contact"] = 7989622789
print(student)
#updating value
student["contact"] = 9885292169
print(student)
print(student.keys())
print(student.values())

#items()
for keys,values in student.items():
    print(keys,values)

print(student.items())

#update
student.update({
    "name" : "raju",
    "contact" : 7989622789
})
print(student)

#pop
student.pop("contact")
print(student)
student.clear()
print(student)

print(student.min())'''

student = {
    "id" : 1,
    "name" : "sai",
    "email" : "dummy@hotmail",
    "cgpa" : 8.11,
    "college" : "jntuh"
}
print(student.items())
print(max(student))
print(min(student))
print(len(student))
print(sorted(student))
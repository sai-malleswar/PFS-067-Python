# def greet():#greet -> function name
#     #function body
#     print("Hello Sir")
# #function calling
# greet()
# function creation using return
# def greet():
#     return "Hello Sir"
# print(greet())

#user defined functions
#Types of functions
#type 1: no parameters and no return values
def greet():
    print("Dattebayo!")
greet()

#type 2: parameters but no return values
def greet(name):
    print("Naruto", name)
greet("uzumaki")

#type 3 : no parameters but return value
def get_number():
    return 100
result = get_number()
print(result)

#type4: parameters and return value
def add(a,b):
    return a + b
print(add(4,3))
#parametrs = variables defined inside the function
#argument = values defined at the time of function calling

def calc(a,b):
    add =a+b
    sub = a-b
    return add,sub
x,y = calc(20,30)
print(x)
print(y)

#positional arguments -> arguments are matched based on their position
def student(name,age):
    print("Name: ",name)
    print("Age: ",age)
student("sai",21)

#keyword arguments
def student(name,age):
    print(name)
    print(age)
student(age=21,name="sai")

#Default arguments
def greet(name="Boruto"):
    print("Hello",name)
greet()

#variable length arguments (*args)
def add(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total
print(add(10,30))
print(add(1,2,3,4,5,6,7,8,9))

#*args = it collects multiple positional arguments into a tuple
# **kwargs = keyword variable length Arguments -> accepts multiple keyword arguments
#**kwargs -> it collects multiple arguments into a dictionary
def student_details(**details):
    print(details)
student_details(
    name = "Boruto",
    age = 19,
    city = "konoha"
)


#combination of *args and **kwargs
def example(*args,**kwargs):
    print(args)
    print(kwargs)
example(10,20,30, name = "Hinata",age = 33)
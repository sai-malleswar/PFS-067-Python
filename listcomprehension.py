#list comprehension: A list comprehension is a short and clean way of creating a list using a loop
#general method:
# numbers = []
# for i in range(1,6):
#     numbers.append(i)
# print(numbers)

#list comprehension method:
# numbers = [i for i in range(1,6)]
# print(numbers)
#one line representation of loop
#syntax: [expression for variable in iterable]
#[x for x in range(1,5)]

# squares = [i * i for i in range(1,6)]
# print(squares)

#list comprehension on strings
# names = ["sai", "mall", "raj"]
# result = [name.lower() for name in names]
# print(result)

#list comprehension with if and for
# numbers = [i for i in range(1,11) if i % 2 == 0]
# print(numbers)

#filtering values
# nums = [10, 15, 20, 25, 30, 35, 40]
# result = [i for i in nums if i > 20]
# print(result)


#Nested list comprehension:
#it means having more than one for loop inside list comprehension
# result  = [(i,j) for i in range(1,4) for j in range(1,4)]
# print(result)

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# result = [x for row in matrix for x in row]
# print(result)

#generators:
#generators produces values one at a time when required

# def numbers():
#     for i in range(1,6):
#         yield i
# print(numbers)

#yield passes the function and remebers its current state.it is used while using generators

# def numbers():
#     for i in range(1,6):
#         yield 1
#         yield 2
#         yield 3
# result = numbers()
# print(result)
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))

# def demo():
#     return 1
#     return 2
# print(demo())
# print(demo())

# def demo():
#     yield 10
#     yield 20
#     yield 30
# result = demo()
# print(next(result))
# print(next(result))
# print(next(result))

#understanding generator execution
# def demo():
#     print("Start")
#     yield 10
#     print("Middle")
#     yield 20
#     print("End")
#     yield 30
# result = demo()
# print(next(result))
# print(next(result))
# print(next(result))

#using generator with for loop
# def nums():
#     for i in range(1,6):
#         yield i
# for x in nums():
#     print(x)


#generator expresion:
#list comprehension = []
#generator expression exp = ()
# nums = (x * x for x in range(1,6))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))

def even():
    for i in range(1,21):
        if i % 2 == 0:
            yield i
for x in even():
    print(x)
#we need to use generators when we want to generate values at a time.
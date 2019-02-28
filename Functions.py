# # # a function is a block of code that isusedto perform a related action
# # # To define a function,we use a keyword called def i.e
# #
# # # creating or defining a function
# # def chapisha (smth):
# #     print(smth)
# #
# # chapisha("Carole")
# # #     Calling a function
# #
# # # Assignment
# #
# # def findgrade(math,eng,kis,science,ssr,):
# #     total=math+eng+kis+science+ssr
# #     average=total/5
# # # We eclare a function then tell it what to do
# # # We first pass the parameters-the columns
# # # Then we pass the arguments
# #
# # # Create a function that takes in name and returns a string in a reversed version
# # name=input("Whats your name ?")
# #
# # def reversemyname(name):
# #     x=name[::-1]
# #     return x
# # reversedname=reversemyname(name)
# # print(reversedname)
#
# # Task 1
# string=input("Whats your response:")
# str(string)
# if string == "Yes":
#     print("Yes")
# elif string == "Yes":
#     print("yes")
# elif string=="YES":
#     print("yes")
# else:
#     print("No")
#
# Task 2
input1=input("Whats input 1:")
input2=input("Whats input 2:")
input3=input("Whats input 3:")
if input1>input2 and input1>input3:
    print(input1)
elif input2>input1 and input2>input3:
    print(input2)
else:
    print(input3)
#
# # Task 3
# programlist=[7,5,10,15,20,25]
# def returnlast(x):
#     x=programlist
#     return x[::4]
# firstandlast=returnlast(programlist)
# print(firstandlast)
# Task 4
number=int(input("Hello there input any number:"))
answer=number%2
if answer==0:
    print("Its an even number Yo")
else:
    print("We dealing with an odd number")

# Task 5


def converttuple(tuples):
    x=tuples[0:5]
    y=tuples[5:]
    return x,y


tuple1={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
tupleconv=list(tuple1)

bothtuples=converttuple(tupleconv)
print(bothtuples[0])
print(bothtuples[1])

# Numpyarrays


#


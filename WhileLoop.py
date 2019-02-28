# Doing something until a condition becomes false.
# A while loop tells python to execute a certain statement or block of statements until a condition is false.
i=0
while i<10:
    i=i+1
    print(i)

numbers=[0,1,2,3,4,5,6,7,8,9]
while len(numbers)>0:
    print(numbers)
    numbers.pop()

# # name=["s","i","s","s","e","y","x","a","v","i","e","r"]
# name=("Carole")
# while len(name)!="d":
#     remo.name[:-1]
#     print(name)

password="input the correct passowrd"
tries=0
while password!="1234" and tries<3:
    password=input("EnteryourPassword")
    tries+=1

if tries>=3:
    print("Pinblocked your card has been swallowed")
else:
    print("Hurray Password is correct")


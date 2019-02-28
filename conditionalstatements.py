# prompts the user to eneter data
marks=int(input("Enter your marks "))

if marks>=350:
    print("Congratulatins you have qualified")
else:
    print("sorry your ass failed")

# Grading system
marks=int(input("Enter your marks "))
average =marks/5
if average>=80 and average <101:
    print("A")

elif average>=70 and average<80:
    print("B")
elif average>=60 and average<70:
    print("C")
elif average>=50 and average <60:
    print("D")
elif average>49 and average>49:
    print("E")
else:
    print("ZZ")
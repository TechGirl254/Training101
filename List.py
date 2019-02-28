# list indexing
daysoftheweek=["monday","tuesday","wednesday","thursday","friday","saturday"]

print(daysoftheweek[0])
# printing out three consecutive days

sublist=daysoftheweek[3:4]
print(sublist)
# terminates at three but position 3 is not included

# details of an individula
details=["carole",24,"carole@gmail.com","Nairobi"]
# list=details
# print=details[:2]
# reversing a string
reverse=details[::-1]
print("reverse",reverse)
# print=reverse[-1:3]


numbers=[0,0,1,2,3,4,5,6,7,8,9]
subnumbers=numbers[-3:-1]
print(subnumbers)

print(set(numbers))

# appending numbers-adding avalue to a list
daysoftheweek.append("val")
print(daysoftheweek)
print(daysoftheweek[-1])
# clears everything from the list
# daysoftheweek.clear()

# extend-merges the lists available
# daysoftheweek.extend()
# print(daysoftheweek)

list1=[0,1]
list2=[2,3]
list3=list1+list2
list1.extend(list2)
print(list3)
print(list1)

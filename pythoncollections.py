thislist = ["apple", "banana", "cherry"]
#thislist[1] = "blackcurrant"
#print(thislist[1:5])
#print(thislist[-4:-1])
#for x in thislist:
   # print(x)
#check if "apple" is present in the list:
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")
#to determine how many items a list has, use the len() method:
print(len(thislist))
#using the append() method to append an item:
thislist.append("orange")
print(thislist)
#To add an item at the specified index, use the insert() method:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
#The remove() method removes the specified item:
thislist.remove("banana")
print(thislist)
#The pop() method removes the specified index, (or the last item if index is not specified):
thislist.pop()
print(thislist)
#The del keyword removes the specified index:
del thislist[0]
print(thislist)
#The del keyword can also delete the list completely:
del thislist
#The clear() method empties the list:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
#Make a copy of a list with the copy() method:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#Make a copy of a list with the list() method:
sjlist = list(thislist)
print(sjlist)

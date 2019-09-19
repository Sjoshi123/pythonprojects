a = "Hello, World!"
b = " Hello, World! "
print(a[1])
print(a[2:5])
print(a[-5:-2])
print(len(a))
print(a.strip()) # returns "Hello, World!"
print(a.lower())
print(a.upper())
print(a.replace("H" , "J"))
print(a.split(",")) # returns ['Hello', 'World!']
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)
y = "ain" not in txt
print(y)
#String Concatenation
c = "Shraddha"
d = "Joshi"
e = c + " " + d
print(e)
age = 36
txt = "My name is Sjoshi, and I am {}"
print(txt.format(age))
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")



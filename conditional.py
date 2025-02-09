#---if/elif/else
'''
age = int(input("Age = "))

if(age >= 18) :
    print("YES")
else :
    print("NO")


marks = int(input("Marks = "))
if(marks <= 100 and marks >= 80):
    print("A+")
elif(marks <= 79 and marks >= 40) :
    print("B")
else :
    print("F")
'''

#---loop er moddhe loop = nested loop ( using a “if” inside an “if” )

#•	Take a num from user and check it is even or odd---
'''
a = int(input("Num = "))
if(a%2 == 0) :
    print("EVEN")
else :
    print("ODD")
'''

#•	Take 3 num from user and find the greatest---
'''
a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))

if(a >= b  and a >= c) :
    print("a")
elif(b >= c) :
    print("b")
else :
    print("c") 
'''

#•	WAP if it is multiple of 7 or not---
'''
a = int(input("Take a number = "))

if(a % 7 == 0) :
    print("Multiple of 7...")
else :
    print("Not multiple of 7...")
'''
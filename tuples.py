#tuple = immutable[change kora jabe na]
#In “List” we use – [ ] and, in “Tuple” we use –  ( )
'''
num = (5,6,7,8)
print(type(num))  #tuple
num = [5,6,7,8]
print(type(num))  #list
'''

# If we want to count a element as ‘tuple’ then we have to use comma after the element Otherwise , python will count that element as normal int number
'''
num = (3)  
print(type(num))   #int
num = (3,)
print(type(num))  #tuple
'''

#[ Tuple slicing same as string slicing and list slicing ]

#---tuple.index (element )---[returns index at the first occurrence]

# num = (1, 2, 3, 4, 5, 6)
# print(num.index(4))

#---tuple.count(element)---[count total occurrence]

# number = (6,4,4,6,0,2,9,9)
# print(number.count(9))

#WAP to count the number of student with the “A” grade in the following tuple.
grade = ("C" , "D" , "A" , "A" , "B" , "B" ,"A")
print(grade.count("A"))
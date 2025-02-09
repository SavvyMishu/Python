#---list.append()---[adds one element at the end]
'''
animal = ["Cat" , "Dog" , "Duck" , "Lion"]
animal.append("Tiger")
print(animal)

info = ["name" , 2233081253 , "cse" , 'b']
info.append(60)
print(info)
'''

#---list.sort()---[sorts in ascending order]
'''
number = [9,2,6,1,5,0,3]
number.sort()   #accending order
print(number)
number.sort(reverse = True)  #decending order
print(number)

animal = ["Cat" , "Dog" , "Duck" , "Lion"]
animal.sort()
print(animal)
'''

#---list.reverse()---[reverse the list]
'''
animal = ["Cat" , "Dog" , "Duck" , "Lion"]
animal.reverse()
print(animal)

number = [9,2,6,1,5,0,3]
number.reverse()
print(number)
'''
#list.insert(idx , element)---[insert element at index]
'''
animal = ["Cat" , "Dog" , "Duck" , "Lion"]
animal.insert(0,"Crocodile")
print(animal)
animal.insert(3,"Parrot")
print(animal)
'''
#---list.remove---[remove first occurrence of element]
'''
num = [5,6,7,8]
num.remove(6)
print(num)
'''
#---list.pop(index)---[remove element at index]
'''
num = [5,6,7,8]
num.pop(3)
print(num)
'''

#---list.copy()---[copy the list]
n = [1,2,3,4]
copied = n.copy()
print(copied)

#---WAP to ask the user to enter names of their 3 favourite movies and store them in a list
'''
movies =[]

movie1 = input("1st movie name is : ")
movie2 = input("2nd movie name is : ")
movie3 = input("3rd movie name is : ")

movies.append(movie1)
movies.append(movie2)
movies.append(movie3)

print(movies)
'''

#WAP to check if a list contains a palindrome of elements. (Hint- use copy( ) method)
'''
num = [1,2,3,4,3,2,1]
num1 = num.copy()
num1.reverse()

if(num == num1) :
    print("YES")
else :
    print("NO")
'''

#sort them["C" , "D" , "A" , "A" , "B" , "B" ,"A"]
grade =["C" , "D" , "A" , "A" , "B" , "B" ,"A"]
grade.sort()
print(grade)
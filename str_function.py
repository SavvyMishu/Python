#---str.endswith(“___”)---
'''
str = "CSE department"
print(str.endswith("nt"))   #---if last indexes matched with the given one it prints True 
print(str.endswith("er"))   #---otherwise False
'''

#---str.capitalized( )---
'''
str = "mishu"
print(str.capitalize())   #---capitalize the 1st char of a string
print(str)   #---purano string tay kono change hobe na
             #---but if we want to store that at the previous string
str = str.capitalize()
print(str)
'''

#---str.replace("old" , "new")---
'''
str1 = "putul"
print(str1)
print(str1.replace("u" , "o"))  #---we can replace char

str2 = "I am a student of UU"
print(str2)
print(str2.replace("student" , "teacher"))   #---we can replace strings
'''

#---str.find("___")---
'''
a = "tithi"
print(a.find("t"))   #---find out the index number that is used at first
print(a.find("o"))   #---if it can't find it then it will print -1

b = "I am a student of CSE department"
print(b.find("CSE")) #---also find the index number of a string that is used at first
'''

#---str.count(___)---
'''
x = "I am a student of CSE department of Uttara University"
print(x.count("a"))       #count kore ekta char koto bar use korchi
print(x.count("of"))      #also count kore ekta string koto bar use korchi
'''

#---WAP to input user's first name and print it’s length-
s = input()
print(len(s))
print("\n")

#---Find the occurance of “$” in a string-
str = "Hi!!! I am the $ symbol...$99,$1000,$10,000"
print(str.count("$"))
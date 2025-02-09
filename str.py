# str1 = "My name is Mishu.\nI a a student."
# print(str1)

# str2 = "Who are you? "
# print(str2)
# str3 = "Do you know me?"
# full_line = str2+" "+str3
# print(full_line)
# print(len(full_line))

# #concatenation---
# print(str2+str3)

# #print the length of a string----
# str4 = "I'm MISHU"
# print(len(str4))

#indexing----------
'''
str = "abcdefghij"
ch = str[3]
print(ch)
print(str[5])
'''

#---slicing => accessing parts of a string------
'''
str = "nothing"
print(str[2:7])
print(str[:5])   #If we don’t write the starting index, python understand that we want to at the first index.(from index 0))
print(str[3:])   #If we don’t write the ending index, python understand that we want to at the last index.
print(str[0:len(str)])
'''

str = "apple"       #---[e = -1 & a = -5]
print(str[-3:-1])   #---negative indexing (from end)
print(str[-5:-1])   #---Last index print nehi hoti…
print(str[-5:0])
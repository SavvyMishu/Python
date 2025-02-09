#sequential traversal

n = [1,2,3,4,5]

for num in n :
    print(num)
else :
    print("END the LOOP")

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
#-------range() Function--------[range(start?,stop,step)]
'''

print(range(5))

for x in range(10):  #sudhu stop valeu dewa
   print(x)    #starts from 0 and ends 10-1 step size(increment)=1

for x in range(2, 6):  #start r stop value dewa
  print(x)

for x in range(1,10,2) :   #start stop step
   print(x)
'''

#print 1-100
'''
for x in range(1,101) :
   print(x)
'''
#print 100-1
'''
for x in range(100,0,-1):
   print(x)
'''
#multiplication table of a number
'''
n = int(input())

for x in range(1,11,1) :
   print(n*x)
'''
#pass statement = null statement
#for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error
'''
for x in range(10) :
   pass
print("spmething........")
'''

#WAP to find the sum of first n numbers---

n = 5

sum = 0
for x in range(1,n+1) :
   sum += x
   
print(sum)

#WAP to find the factorial of first n numbers---

number = int(input())
multi = 1

for i in range(1,n+1) :
   multi *= i
result = multi%1000
print(result)


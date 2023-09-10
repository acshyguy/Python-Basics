#CLASS ACTIVITY 1

#Write a python program to count occurrence of a substring in a string.
#Sample Input: The quick brown for jumps over the lazy dog.
#Substring: fox
#Sample Output: 1

###SOLUTION      
##a= 'The quick brown fox jumps over the lazy dog.'
##      
##a.count('fox')
##print(a.count('fox'))
##
###CLASS ACTIVITY 2
###Write a Python program to remove characters that have odd index values in a given string.
### Sample Input:  ABCDEF PYTHON STRING
### Sample Output: ACE    PTO    SRN
##
### SOLUTION
##a = ("ABCDEF", "PYTHON", "STRING")
##for a in range(0::2):
##    print(a)

## CONTINUE and BREAK Statements
##str="python"
##for x in str:
##    if x in "aeiou":
##        continue
##    print(x)
##else:
##    print("Completed")

##str="python"
##for x in str:
##    if x in "aeiou":
##        break
##    print(x)
##else:
##    print("Completed")

###Eg1
##num=1234
##sum=0
##while num > 0:
##    sum +=num/10
##    num=num//10
##print(sum)

####Eg 2
##l = ["123", 754,21]
##for num in l:
##    sum= 0
##    for i in str(num):
##        sum+= int(i)
##    print(sum)

##def add(a, b):
##    return a+b
##print(add(a=10, b=20))

### Defualt Argument
##def add(a, b=20):
##    return a+b
##print(add(10))

###Variable Argument
##def m1(**x):
## for k, v in x.items():
##    print(x)
##m1(a=10, b=20, c=30)
##m1(id=100, name="Subbalaxmi")




###03-07-23
###SG class
##l = [10,20, 30,40]
##s= filter(lambda x:x>20, l)
##print(list(s))

####Print even numbers
##lst = [1,2,3,4,5,6,7,8,9,10]
##s = filter(lambda x: x%2, lst)
##print(list(s))

####reduce()
##from functools import reduce
##l = [1,2,10,15]
##s=reduce(lambda x,y: x+y, l)
##print(list(s))


##from functools import reduce
##num=int(input("Enter a number:"))
##f = reduce (lambda x,y: x*y, range(1, num+1))
##print(f)

###Recursive()
###Addition
num = 13764
def sum(num):
    if num == 0:
        return 0
    else:
        return((num%10) + sum(num//10))
        
print(sum(num))

#Multiplication
num = 13764
def product(num):
    if num == 0:
        return 1
    else:
        return((num%10) * product(num//10))
        
print(product(num))

##Finding range of sum and product
t = range(1,1001)
s = filter(lambda x: sum(x)==product(x), t)
h=list(s)
print(h)

    












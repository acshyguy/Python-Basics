#1
num = 1
print("num == 1 condition gives:", (num == 1))
if num == 1:
    print("if block statements executed")
else:
    print("else block statements executed")

#2
num = 11
print("num == 11 condition gives:", (num == 11))
if num %2 == 0:
    print("num is an even number")
else:
    print("num is not an even number")

#3
print("Please enter the value from 0 to 4")
x = int(input("Enter a number: "))
if x==0:
    print("You entered: ", x)
elif x==1:
    print("You entered: ", x)    
elif x==2:
    print("You entered: ", x)
elif x==3:
    print("You entered: ", x)
elif x==4:
    print("You entered: ", x)
else:
    print("Beyond the range than specified")

#4
x=int(input("Enter First number: "))
y=int(input("Enter Secondary Number: "))
if x>y:
    print("Biggest Number is: ",x)
else:
    print("Biggest Number is: ",y)



### FUNCTION
##def display():
##    print("welcome to function")
##display()
##display()
##
##
###DEFINING A FUNCTION
##def sum(a,b):
##    print("Sum of two values= ", (a+b))
##sum(20,30)


##height = 30
##base = 13
##area = 1/2(base)* height
##
##def angleArea(base,height):
##    print("")



###Finding Area of a triangle
###Classwork 1
##def angleArea(area, height):
##    print("Ur area of a triangle is: ",base*height/2)
##    
##base = int(input("Enter ur base: "))
##height = int(input("Enter ur height: "))
##Calling a function
##angleArea(base, height)

###Or(Using a RETURN)
##def angleArea():
##    area = base*height/2
##    return area
##base = int(input("Enter ur base: "))
##height = int(input("Enter ur height: ")) 
##
##x=angleArea()
##print("Ur area of a triangle is:", x)

#Returning multiple values
def m1(a,b):
    c = a+b
    d = a-b
    return c, d
#calling function
x,y = m1(10,5)
print("Sum of a and b: ",x)
print("subtraction of a and b:", y)

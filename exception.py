###Exception Handling
##x= 123
##if x==123:
##    print("Hello")

####Exception try and catch
##print('One')
##print('Two')
##try:
##    print(10/0)
##except ZeroDivisionError:
##    print("Exception passed")
##print('Four')

###Eg To prompt a user to enter a number that is not 0 and is not any other data type
###aside int. When 0 or non integer value is entered, throw an error.
##x = int(input("Enter a number: "))
##y = int(input("Enter another number: "))
##
##def division(x,y):
##    if x or y != 0 or (x,y) == int:
##        try:
##            z = x/y
##            return z
##            #print("type a correct number!")
##                
##        except ZeroDivisionError and ValueError:
##            print("type a correct number!")
##print(division(x,y))         


###Eg of writing our own error exception 
##try:
##    x=int(input("Enter a number between positive integer:"))
##    if x < 0:
##        raise ValueError(x)
##except ValueError as e:
##    print("You provided {}. Please provide positive interger value only".format(e))
##







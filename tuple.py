### TUPLE
##name = ("Sushanth")
##print(name)
##print(type(name)) #This returns string
###Eg1
##a = (11)
##print(a)
##print(type(a))
###Eg2
##name = ("Sushanth",)
##print(name)
##print(type(name)) # This returns tuple coz of the comma(,).
#Eg 3
##name = ("Sam",16, "Lagos","Student")
##print(name)
##print(type(name))

###range = (0, 16) 
##l = [11, 22, 33]
##t = tuple(l)
##print(t)

####OR Odd numbers from 0 to 15
##t = tuple(range(1, 16, 2))
##print(t)

####Class work. Having 2 functions, 1st for signup(), having username & password.
#### 2nd for login()  
##username = str(input("Enter ur username: "))
##password = int(input("Enter ur password: "))
##def signUp():
##    userInfo = username, password
##    return userInfo
##x = signUp()
##print("User name and password are:", x)
##
##def login():
##    return x
##print(login())

###Eg 4
##t=(10,20,30,40,50,60)
##print(t[2:5])
##print(t[2:100])
##print(t[::2])

###Multiplication()
##t1=(10, 20, 30, 40)
##t2=t1*3
##print(t2)

### min() and max()
##t = (10, 20, 10, 10, 20)
##print(min(t))
##
##t = (10, 20, 10, 10, 20)
##print(max(t))

####PACKING()
##a=10
##b=20
##c=30
##d=40
##t=a, b, c, d
##print(t)
##
####UNPACKING()
##t=(10, 20, 30, 40)
##a, b, c, d = t
##print("a=",a ,"b=",b, "c=",c ,"d=",d)


##userdetail = ("Ayo","Male",17)
##name, sex, age = userdetail
##print(age)
##print(contact)
##
##name, sex, age, contact = userdetail

####
##studentdetail = ("Ayo","Male",17,"Economics", "419yan")
###name, sex, age = studentdetail #This will throw an errorcoz not all the arguments are given
##name, sex, *other = studentdetail #Used when we dont want to list all the arguments
##print(other)
###print(age)
###print(contact)








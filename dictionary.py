#### DICTIONARY
##d = {}
##d[1] = "Ramesh"
##d[2] = "Suresh"
##d[3] = "Mahesh"
##print(d)
####Or
##d = {1:"Ramesh", 2:"Arjun", 3:"Nireekshan"}
##d[4] = "Ayo"
##print(d)

##d = {}
##n=int(input("Enter number of employees:"))
##i=1
##while i <= n:
##    name= input("Enter Employee Name:")
##    salary= input("Enter Employee salary:")
##    d[name]=salary
##    i=i+1
##for x in d:
##    print("The name is:", x,"and his salary is:", d[x])

###Delete() 
##d={1: 'Ayo',2:'Suresh', 3:'Mahesh'}
##print("Before deleting key from dictionary", d)
##del d[1]
##print("After deleting key from dictionary", d)
##
###dict()
##d= dict()
##print(d)
##print(type(d))

###get()
##d={1: 'Ayo',2:'Suresh', 3:'Mahesh'}
##print(d.get(1))

###copy()
##d={1: 'Ayo',2:'Suresh', 3:'Mahesh'}
##d.copy
####print(d)
##
###Item()
##d={1: 'Ayo',2:'Suresh', 3:'Mahesh'}
##print(d.items())
##print(d)

#keys()
d = {1: 'Ramesh', 2:'Suresh', 3: 'Mahesh'}
print(d)
for k in d.keys():
    print(k)
#values()
d = {1: 'Ramesh', 2:'Suresh', 3: 'Mahesh'}
print(d)
for k in d.values():
    print(k)










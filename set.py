##s = {10,20, 30, 40}
##print(s)
##print(type(s))

##s = {10,'20','Rahul',234.56, True}
##print(s)
##print(type(s))

#### Add()
##s={10, 20, 30}
##s.add(40)
##print(s)
##
#### Update()
##s={10,20,30}
##l=[40, 50, 60, 10]
##s.update(l)
##print(s)
##
##s={10,20,30}
##l=[40, 50, 60, 10]
##s.update(l, range(5))
##print(s)

#### Pop() #This removes randomly
##s={10,30,40,20,300}
##print(s)
##print(s.pop())
##print(s)

####Remove() ##When we put element that is not in the set, it throws error
##s={40,10,30,20}
##s.remove(30)
##print(s)

##s.remove(50) 
##print(s)

#### Discard()  ##When we put element that is not in the set, it won't error
##s={40,10,30,20}
##s.discard(10)
##print(s)
##
##s.discard(50) 
##print(s)

#### Union() #returns the element they have in common
##x={10,20,30,40}
##y={30,40,50,60}
##print(x.union(y))
##
#### Interset()
##x={10,20,30,40}
##y={30,40,50,60}
##print(x.intersection(y))

#### Difference() #returns element in x but not in y
##x={10,20,30,40}
##y={30,40,50,60}
##print(x.difference(y))
##print(x-y)
##print(y-x)
###Symetric_difference()
##x={10,20,30,40}
##y={30,40,50,60}
##print(x.symmetric_difference(y))
##print(x^y)

#### superset() # >= or <= is used
##A={1,2,3,4}
##B={1,2,3,4,5,6,7,8,9,10}
##print(A>=B)

####SET COMPREHENSION
##s={x*x for x in range(5)}
##print(s)

####REmoving Duplicate Elements ##Set does not hv duplicate but when we use list,
#### we convert to set to be able to remove duplicate
##l=[10,20,30,10,20,40]
##s=set(l)
##print(s)


# #Frozen Set
vowels = ('a', 'e', 'i', 'o', 'u')
fSet = frozenset(vowels)
print(fSet)
print(type(fSet))






### LIST
##l = [1,2,3,4,5,6]
##print(l)
##print(type(l))
##
###ASSINING AND REPLACE AN INDEX
##print("Before modifying l[0]:", l[0])
##l[0] = 20
##print("After modifying l[0]:", l[0])
##print(l)
##
###CONVERTING FROM RANGE TO LIST
##r = range(0, 10)
##l = list(r)
##print(l)

### Eg, Slicing
##n = list(range(1, 7))
##print(n)
##
##print(n[2:5:2])
##print(n[4::2])
##print(n[3:5])

### How to get a list of duplicate numbers. n = [1,2,3,5,5,5,3]
##n = list(range(1, 6)) + [5,5] + list(range(3,4))
##print(n)

### INSERT METHOD
##n = [10, 20, 30, 40, 50]
##n.insert(0, 76)
##print(n)
###Eg 2
##l = [10, 20, 30, 40]
##print(l)
##l.insert(1, 111)
##print(l)
##l.insert(-1, 222)
##print(l)
##l.insert(10, 330)
##print(l)
##l.insert(-10,444)
##print(l)
##l.insert(-4, 700)
##print(l)

###EXTEND METHOD
##l1 = [1,2,3]
##l2 = ['Rahul', 'Rakesh', 'Regina']
##print('Before extend l1 is:', l1)
##print('Before extend l2 is:', l2)
##l2.extend(l1)
##print('After extend l1 is: ', l1)
##print('After extend 12 is:', l2)

###Eg 2
##def sum(august_txns,sept_txns):
##    print("Sum of two values= ", (august_txns+sept_txns))
##sum(august_txns,sept_txns)
##
##august_txns = [100, 200, 500, 900]
##sept_txns = [111, 222, 333, 600, 790, 100, 200]
##print("August month transactions are: ",august_txns)
##print("September month transactions are: ",sept_txns)
##sept_txns.extend(august_txns)
##print("August and Sept total transactions amount: ", sum(sept_txns))

### REMOVE. this removes the value and does not return any value
##n= [1,2,3,1]
##n.remove(1)
##print(n)

### POP Method. removes the last index
##n= [1,2,3,4,5,6,7]
##print(n.pop(1))
##print(n)
##print(n.pop())
##print(n)

### Reserve
##n= [1,2,3,4,"two"]
##print(n)
##n.reverse()
##print(n)

### Sort()
##n= [1,8,87,4]
##print(n)
##n.sort()
##print(n)

##s= ["Kalu","Ramesh","April"]
##s.sort()
##print(s)

### Reverse()
##s= ["Kalu","Ramesh","April"]
##s.sort(reverse=True)
##print(s)

### Cloning using slicing operator
##x= [10, 20, 30]
##y=x
##print(x)
##print(y)
##print(id(x))
##print(id(y))
##
##x[1] = 99
##print(x)
##print(y)
##print(id(x))
##print(id(y))

## Cloning using copy() method
##x= [10, 20, 30]
##y=x.copy()
##print(x)
##print(y)
##print(id(x))
##print(id(y))
##
###CONCANTENATION
##a = [1,2,3]
##print(a)
##print(2*a)

#COMPARISON
##print([1,2,3]<[2,2,3])
##print([1,2,3]<[1,2,3])
##print([1,2,3]<=[1,2,3])
##print([1,2,3]<[1,2,4])
##print([1,2,3]<[0,2,3])
##print([1,2,3]==[1,2,3])

## NESTED LIST
#a = [80,90]
#b = [10, 20, 30, a]
##print(b[0])
##print(b[1])
##print(b[2])
##print(b[3])

###Filter
##items_cost = [999, 888,1100,1200, 1300, 777]
##gt_thousand = filter(lambda x : x>1000, items_cost)
##x = list(gt_thousand)
##print("Eligible for discount: ", x)
##
###Map
##without_gst_cost = [100, 200, 300, 400]
##with_gst_cost = map(lambda x: x+10, without_gst_cost)
##x=list(with_gst_cost)
##print("Without GST items costs:", without_gst_cost)
##print("With GST items costs: ", x)

###Reduce()
##from functools import reduce
##each_items_costs = [111, 222, 333, 444]
##total_cost = reduce(lambda x,y: x+y, each_items_costs)
##print(total_cost)

###List Comprehension. Eg multiplying by 2
##x=[1,2,3,4]
##y=[]
##for i in x:
##    y.append(i*2)
##print(y)
###Eg 1 when writing in a single line usin comprehension
##x=[1,2,3,4]
##y=[i*2 for i in x]
##print(y)
###Eg 2
##s= range(1, 20, 3)
##for i in s:  #this loop is used to know whats in  s
##    print(i)
##m= [x for x in s if x%2 == 0]
##print(m)







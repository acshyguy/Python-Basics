###1 While Loop
##x=1
##while x<=5:
##    print(x)
##    x+=1
##print("End")
##
###2
##x=10
##while(x>=10) and (x<=20):
##    print(x)
##    x+=2
##print("End")
#3
##item_costs = [10, 20, 30]
##sum=0
##for x in item_costs:
##    sum=sum + x
##print(sum)
##
###4 Checking for Even Numbers
##item_costs = [10, 20, 25, 27, 28, 35, 63, 71, 101, 3]
##sum = 0
##for x in item_costs:
##    if (x%2 == 0):
##        sum= sum+x
##print(f"The sum of the even numbers are {item_costs} is {sum}")


#5 Nested Loop
##rows = range(1, 5)
##for x in rows:
##    for star in range(1, x+1):
##        print('*', end='')
##    print()

#6 To find range of 20 numbers in a straight line, seperated by space 
##rows = range(1, 21)
##for x in rows:
##    print(x, end= ' ')

###7 For finding odd numbers from 1 to 100
##for num in range(1, 100, 2):
##    print(num, end= ' ')

###8 Break Statement
##group = [1,2,3,4]
##search = int(input("Enter the element here: "))
##for item in group:
##    if search == item:
##        print("Item found in the group")
##        break
##
##
###9 Continue
##cart=[10,20,500,700,50,60]
##for item in cart:
##    if item>=500:
##        continue
##    print("item:",item)

#10 Loop with else if
group = [1, 2, 3, 4]
search= int(input("Enter the element in search: "))
for element in group:
    if search == element:
        print("element found in group")
        break
else:
    print("Element not found")

# DO WHILE LOOP
total = 0
#loop wiil run at least once
while True:
    # Ask the user to enter a number
    num = int(input("Enter a number(or 0 to exit): "))
    if num == 0:
        break
    total += num
# print the total    
print("Total:", total)
    
    

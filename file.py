##f=open("firstFile.txt", 'w')
##print("File Name:", f.name)
##
##print("File Mode:", f.mode)
##
##print("Is File Readable:", f.readable())
##
##print("Is File Writeable:", f.writable())
##
##print("Is File Closed:", f.closed)
##f.close()
##
##print("Is File Closed:", f.closed)


##f=open("wish.txt", 'w')
##
##f.write("Welcome\n")
##f.write("to\n")
##f.write("python world\n")
##print("Data written to the file succesfully")
##f.close()

import csv
with open('employee.csv', 'w', newline ='') as a:
    docs = csv.writer(a)
    docs.writerow(['EMP NO', 'EMP NAME', 'EMP SAL', 'EMP ADDRESS'])
    n = int(input('Enter Number of Employees: '))
    for i in range(n):
        eno = input('Enter Employee No: ')
        ename = input('Enter Employee Name: ')
        esalry = input('Enter Employee Salary: ')
        eaddr = input('Enter Employee Address: ')
        docs.writerow([eno, ename, esalry, eaddr])
print('Total employee data written to file successfully')

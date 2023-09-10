# import pyodbc

# conn = pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server;SERVER=ISW2-220502-471\SQLEXPRESS01;DATABASE=Training;Trusted_Connection=yes;')

# cur=conn.cursor()
# cur.execute('SELECT * FROM Training.dbo.job_Employee')

# for row in cur:
#     for value in row:
#         print(value,end=' , ')
#     print()

# conn.close()


## Prompting user to input INSERT METHOD
# cur=conn.cursor()

# #Course_Id = int(input("Enter ur Course Id:"))
# Course_Title = input("Enter ur Course Title:")
# Course_Code = (input("Enter ur Course Code:"))
# Course_Tutor = input("Enter ur Course Tutor:")

# cur.execute('insert into Training.dbo.studentCourse_Syllabul values(?,?,?)',(Course_Title, Course_Code, Course_Tutor))

# cur.commit()

# conn.close()

# ##Prompting user to input UPDATE METHOD
# cur=conn.cursor()
# Course_Id = int(input("Enter ur Course Id for Update:"))
# Course_Title = input("Enter ur Course Title:")
# Course_Code = input("Enter ur Course Code:")
# Course_Tutor = input("Enter ur Course Tutor:")

# cur.execute('update Training.dbo.studentCourse_Syllabul set Course_Title=?,Course_Code=?, Course_Tutor=? where Course_Id=?',(Course_Title, Course_Code, Course_Tutor, Course_Id))

# cur.commit()

# conn.close()

# ##Prompting user to input DELETE METHOD
# cur=conn.cursor()
# Course_Id = int(input("Enter ur Course Id for DELETE:"))

# cur.execute('delete Training.dbo.studentCourse_Syllabul where Course_Id=?',(Course_Id))

# cur.commit()

# conn.close()

####Prompting user to input SELECT By ID METHOD
# def selectById():
#     cur=conn.cursor()
#     Course_Id = int(input("Enter ur Course Id for DELETE:"))

#     cur.execute('select * from Training.dbo.studentCourse_Syllabul where Course_Id=?',(Course_Id))

#     for row in cur:
#         for value in row:
#             print(value,end=' , ')
#     print()

#     cur.commit()

#     conn.close()
# selectById()


### Creating a Table 
# import pyodbc
# try:
#     conn = pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server;SERVER=ISW2-220502-471\SQLEXPRESS01;DATABASE=Training;Trusted_Connection=yes;')

#     cursor=conn.cursor()

#     cursor.execute("create table Training.dbo.job_Employee(emp_no int, emp_firstName varchar(225), emp_lastName varchar(225), emp_salary decimal(10,2), emp_address varchar(225))")

#     print("Job_Employee table created succesfully")
#     conn.commit()

# except pyodbc.Error as e:
#     if conn:
#         conn.rollback()
#         print(e)
# finally:
#     if cursor:
#         cursor.close()
#     if conn:
#         conn.close()
    
#     conn.close()

### INSERT
import pyodbc
try:
    conn = pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server;SERVER=ISW2-220502-471\SQLEXPRESS01;DATABASE=Training;Trusted_Connection=yes;')

    cursor=conn.cursor()

    sql="insert into Training.dbo.job_Employee values(?,?,?,?,?)"
    records= [()]

    print("Job_Employee table created succesfully")
    conn.commit()

except pyodbc.Error as e:
    if conn:
        conn.rollback()
        print(e)
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
    
    conn.close()
##import arithmetics
##
##print(arithmetics.x)
##
##arithmetics.sum(1,2)
##arithmetics.subtraction(10,2)
##arithmetics.multiplication(12,2)
##arithmetics.division(2,45)

## ANOTHER IMPORT METHOD 2
##from arithmetics import x, sum
##print(x)
##sum(21,43)


### ANOTHER IMPORT METHOD 3
##from arithmetics import *
##print(x)
##sum(45,76)
##multiplication(6,89)

### FOR RELOADING OF FILES AFTER EDITH
##import arithmetics
##from imp import reload

##import arithmetics
##print (dir())
##
##dir() in arithmetics
##print(dir())

# PACKAGE IMPORTATION
import operations.arithmetics as calculator

calculator.sum(1,2)
calculator.subtraction(10,2)
calculator.division(2,45)
calculator.multiplication(12,2)

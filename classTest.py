### QUESTION 1 Concatenate two lists index-wise
##list1 = ["M", "na", "i", "ke"]
##list2 = ["y", "me", "s", "lly"]
##
##answer = []
##
##for i in range(len(list1)):
##    concatenated_result = str(list1[i]) + str(list2[i])
##    answer.append(concatenated_result)
##
##print(answer)

### QUESTION 2 Remove all occurrences of a specific item from a list.
##list1 = [5, 20, 15, 20, 25, 50, 20]
##
##
##duplcateRemoval = []
##for item in list1:
##    if list1.count(item) == 1:
##        duplcateRemoval.append(item)
##
##print(duplcateRemoval)

### OUESTION 3 Create a string made of the middle three characters
## Case1
##str1 = "jhonDipPeta"
##leftLen = 4
##rightLen = 4
##
##newWord = str1[leftLen:len(str1)-rightLen]
##print(newWord)
##
## Case2
##str2 = "JaSonAy"
##leftLen = 2
##rightLen = 2
##
##newWord = str2[leftLen:len(str2)-rightLen]
##print(newWord)

# QUESTION 4 Write a program to create a recursive function to cal. the sum of numbers from 0 to 10.
##sum = 0
##for i in range(11):
##    sum += i
##print(sum)



### QUESTION 5 Find the largest item from a given list using list comprehension
##x = [4, 6, 8, 24, 12, 2]
##
##largestItem = max(x)
##print(largestItem)


##TAKE HOME ASSIGNMENT
###QUSTION 1
##Write a program which takes 5 names in a list
##then sort the list based on the string length
#Solution
##names =["Ayo", "Abel", "Rakesh", "Johnson", "Precious"]

def nameSorting(names):
    names.sort(key=len)
    return names

namesList = ["Ayo", "Precious", "Abel", "Rakesh", "Johnson"]
sortedNames = nameSorting(namesList)

print(sortedNames)


###QUSTION 2
##Write a programm which has a list of trainees full name,
##create a dictionary where the initial is the key and surname is the value
# Solution
def create_initial_surname_dictionary(names):
    initials_surnames = {}
    for name in names:
        parts = name.split()
        if len(parts) >= 2:
            initial = parts[0][0]
            surname = parts[-1]
            initials_surnames[initial] = surname
    return initials_surnames
#create_initial_surname_dictionary(names)

trainees_names = ['John Smith', 'Alice Johnson', 'Michael Brown', 'Emily Davis']
initial_surname_dict = create_initial_surname_dictionary(trainees_names)
print(initial_surname_dict)



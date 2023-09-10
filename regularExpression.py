#import re

# count = 0
# pattern = re.compile("ab")
# matcher = pattern.finditer("abaababa")
# for match in matcher:
#     count += 1
#     print(match.start(), "...", match.end(), "...", match.group())
#     print("The number of occurrences:", count)

# ## Eg 2 without matcher

# count = 0
# matcher = re.finditer("ab","abaababa")
# for match in matcher:
#     count += 1
#     print(match.start(), "...", match.end(), "...", match.group())
#     print("The number of occurrences:", count)

# import re
# matcher=re.finditer("[a-zA-Z0-9]", "a7b@k9z")
# for match in matcher:
#     print(match.start(), "...", match.group())

# import re
# matcher = re.finditer("[^a-zA-Z0-9]", "a7b@k9z")
# for match in matcher:
#     print(match.start(), "...", match.group())

# ##Predefined Character
# #For small s
# import re
# matcher = re.finditer("\s","a7b @k9z")
# for match in matcher:
#     print(match.start(), "...", match.group())
# #For dot(.)
# import re
# matcher = re.finditer(".","a7b @k9z")
# for match in matcher:
#     print(match.start(), "...", match.group())
# #For Small w
# import re
# matcher = re.finditer("\w","a7b @k9z")
# for match in matcher:
#     print(match.start(), "...", match.group())
# # For small s
# import re
# matcher = re.finditer("\s","a7b @k9z")
# for match in matcher:
#     print(match.start(), "...", match.group())

# #For big S
# import re
# matcher = re.finditer("\S","a7b @k9z")
# for match in matcher:
#     print(match.start(), "...", match.group())

# #For a
# matcher = re.finditer("a","abaabaaab")
# for match in matcher:
#     print(match.start(), "...", match.group())
# #For a+
# matcher = re.finditer("a+","abaabaaab")
# for match in matcher:
#     print(match.start(), "...", match.group())

# #For a*
# matcher = re.finditer("a*","abaabaaab")
# for match in matcher:
#     print(match.start(), "...", match.group())

# #For a?
# matcher = re.finditer("a?","abaabaaab")
# for match in matcher:
#     print(match.start(), "...", match.group())

# #For a{m}
# matcher = re.finditer("a{3}","abaabaaab")
# for match in matcher:
#     print(match.start(), "...", match.group())

# #For a{m,n}
# matcher = re.finditer("a{2,4}","abaabaaab")
# for match in matcher:
#     print(match.start(), "...", match.group())



##Class Work  #To get email in the setting below
## "segun.ade@gmail.com" 

##Atempt 1
# pattern = "segun.ade@gmail.com"
# matcher = re.finditer("[a-zA-Z0-9]+[.][a-zA-Z0-9]+[@][a-zA-Z]+[.][a-z]{3}", pattern)
# for match in matcher:
#     print(match.start(), "...", match.group())

# # Correct Solution 
# def test():
#     count=0
#     matcher = re.finditer("\w +\ . \w + @ \w + \. \w{3}", "segun.ade@gmail.com")
#     for match in matcher:
#         print(match.start(), "...", match.group())
#         print("The number of occurrence:", count)

##For Phone number



# #search()
# import re
# s= input("Enter pattern to check: ")
# m= re.search(s, "abaaaba")
# if m != None:
#     print("Match is available")
#     print("First Occurrence of match with start index:", m.start(), "and end index:", m.end())
# else:
#     print("Match is not available")

# #findall()
# import re
# l= re.findall("[0-9]", "a7b9c5kz")
# print(l)

# #sub()
# import re
# s= re.sub("[a-z]", "#", "a7b9c5k8z")
# print(s)

# #split()
# import re
# l= re.split(",", "KGF, BB1, BB2")
# print(l)
# for t in l:
#     print(t)

# #subn()
# import re
# t= re.subn("[a-z]", "#", "a7b9c5k8z")
# print(t)
# print("The Result String:", t[0])
# print("The number of replacements:", t[1])


## Writing a correct gmail id
# import re
# s=input("Enter Mail id:")
# m=re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com", s)
# if m != None:
#     print("Valid Mail Id")
# else:
#     print("Invalid Mail Id")

### Extraction of mobile numbers from text 
# # The sample format is below
# import re
# f1=open("input.txt", "r")
# f2=open("output.txt", "w")
# for line in f1:
#     items = re.findall("[7-9]\d{9}",line)
#     for n in items:
#         f2.write(n+"\n")
# print("Extracted all Mobile Numbers into output.txt")
# f1.close()
# f2.close()
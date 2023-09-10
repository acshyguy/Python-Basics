#SPLIT METHOD
message="Python programming language"
n=message.split()
print("Before splitting: ",message)
print("After splitting: ",n)
print(type(n))
for x in n:
    print(x)


#JOIN METHOD
profile = ['Roshan', 'Actor', 'India']
candidate = '-'.join(profile)
print(profile)
print(candidate)

profile = ['Roshan', 'Actor', 'India']
candidate = '/'.join(profile)
print(profile)
print(candidate)

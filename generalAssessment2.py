# def triplePythagorean(sum_value):

#     for m in range(2, int(sum_value**0.5)):
#             if sum_value % m == 0:
#                 n = sum_value // m
#                 k = 1
#                 while m > n:
#                     a = k * (m**2 - n**2)
#                     b = 2 * k * m * n
#                     c = k * (m**2 + n**2)
#                     if a + b + c == sum_value:
#                         return a, b, c
#                     k += 1
#                     n = sum_value // (m * k)
#             m += 1
#     return None
# sum_value = 1000
# triplet = triplePythagorean (sum_value)

# if triplet is not None:
#     a, b, c = triplet
#     product = a * b * c
#     print(f"The special Pythagorean triplet for sum {sum_value} is: ({a}, {b}, {c})")
#     print(f"The product of the triplet elements is: {product}")
# else:
#     print(f"There is no special Pythagorean triplet for sum {sum_value}.")
# triplePythagorean(sum_value)

# No 3
def prime(num):
    return num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))

def primeGenerator(start, end):
    return (num for num in range(start, end + 1) if prime(num))
# print(primeGenerator)

start_num = 10
end_num = 30

print(f"Prime numbers between {start_num} and {end_num}:")
for prime in primeGenerator(start_num, end_num):
    print(prime)
print(primeGenerator)
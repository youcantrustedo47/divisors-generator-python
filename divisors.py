'''

Divisors generator

by trustnoedo


'''


# Function
def divisors(x):
    l = []
    lstrng = list(range(1, x+1))
    for i in lstrng:
        if x % i == 0:
            l.append(i)
    return l


# Introduction
print()
print("--------------------")
print()
print("Hi! Welcome to the program!")
print("Here you'll be able to find out "
      "all the divisors of a number that you choose!")
print()
print("--------------------")
print()

# Storing and calling the function
n = int(input("Insert your number: "))
print()
print("...")
print()
print("Here are all the divisors!")
print()

result = divisors(n)
for i in result:
    print(i)

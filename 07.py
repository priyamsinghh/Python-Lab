base = int(input("Enter base:"))
exponent =int(input("Enter Exponent:"))

result = 1

for exponent in range(exponent, 0, -1):
    result *= base

print("Answer = " + str(result))
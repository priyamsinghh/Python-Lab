# Python code to demonstrate naive
# method to compute gcd ( recursion )


def hcf(a, b):
	if(b == 0):
		return a
	else:
		return hcf(b, a % b)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("The gcd of ",num1,"and ",num2, "is : ", end="")
print(hcf(num1, num2))

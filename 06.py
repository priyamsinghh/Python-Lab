def newtonsqrt(n):
    d=0.5*n
    f=0.5*(d+n/d)
    while f!=d:
        d=f
        f=0.5*(d+n/d)
    return d

a=int(input("Enter a number:"))
print("Square root of ",a," is:",newtonsqrt(a))
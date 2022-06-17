ls = list(int(x) for x in input("Enter initial values of stack:\t").split())
print("Enter:\n1 for Push\n2 for Pop\n3 for display\nOther value to exit")
while(True):
    x = int(input("Enter your choice:\t"))
    if x == 1:
        ls.append(int(input("Enter value to Push:\t")))
    elif x == 2:
        if len(ls) == 0:
            print("Stack Underflow")
        else:
            print("Value Poped:\t", ls.pop())
    elif x == 3:
        print("Your Stack is:\t", ls)
    else:
        break
print("Your Stack is:\t", ls)

tup = ("apple", "banana", "cherry")
print("Tuple:",tup)
print("Length:",len(tup))
print("Type: ",type(tup))
y = list(tup)
y[0] = "kiwi"
tup= tuple(y)
print("Updated Tuple:",tup)
y.append("orange")
print("Appended Tuple:",y)
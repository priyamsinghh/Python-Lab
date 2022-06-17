# Python program to demonstrate working
# of dictionary copy
dic = {1:'Hello', 2:'Good', 3:'Morning'}
dic2 = {3:'AfterNoon'}
print('original: ', dic)
print(dic.get(1))
print(dic.keys())
print(dic.values())
print(dic.items())
new = dic.copy()
print("New dic:",new)
dic.update(dic2)
print("Updated dic:",dic)
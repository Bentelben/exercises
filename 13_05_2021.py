print("№1")
a = input()

print(a[2])
print(a[-2])
print(a[:5])
print(a[:-2])
print(a[::2])
print(a[1::2])
print(a[::-1])
print(len(a))


print("№2")
a = input()
b = -(len(a)//2)
print(a[b:] + a[:b])

print("№3")
a = input()
a = a.split(" ")
print(a[1], a[0])

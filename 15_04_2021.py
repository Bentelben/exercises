############################
print() # 5.34
############################

s = 1
h = 1
for i in range(0, 9):
    h *= 3
    s += 1/h

print("5.34: " + str(s))

############################
print() # 5.35
############################

n = int(input("5.35 Enter N: "))
s = 1
h = 1
for i in range(1, n):
    h += 1
    s += ((i%2)*-2 + 1)*(1/h)

print("5.35: " + str(s))

############################
print() # 5.61
############################

print("5.61 Enter Nums: ")
n = 0
s = []
while(True):
    h = input()
    if h=="":
        print("Next class: ")
        break
    n += 1
    s.append(int(h))
h = []
for i in range(0, n):
    h.append(int(input()))

print("5.56 First: " + str(sum(s)//len(s)) + " Second: " + str(sum(h)//len(h)))

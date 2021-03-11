n = int(input())

a3 = n//60
n -= a3*60

a2 = n//10
n -= a2*10

a1 = n


if a1*15 > 125:
    a1 = 0
    a2 += 1

if a1*15 + a2*125 > 440:
    a1 = 0
    a2 = 0
    a3 += 1

print(a1, a2, a3)

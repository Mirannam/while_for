cond1 = []
cond2 = []
for i in range(-100,101):
    if i %13 == 0 and i % 2 ==0:
        a = i**2
        print(a)
        cond1.append(a)
print(cond1)
print(len(cond1))
for i in range(-100,101,7):
    if i % 2 != 0:

        cond2.append(i)
print(cond2)
print(len(cond2))
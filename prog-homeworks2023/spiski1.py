import random
a=random.randint(50,101)
b=random.randint(50,101)
a1=[1, 2, 3, 4, 5, 6, 7, 8, 9]
b1=[2, 10, 85, 1, 100, 1120, 1234]
f=0
while a>0:
    f=str(random.randint(0,10000))
    if f not in a1:
        a1.append(f)
        a-=1
while b>0:
    f=str(random.randint(0,10000))
    if f not in b1:
        b1.append(f)
        b-=1
for i in a1:
    if i not in b1:
        print (i)


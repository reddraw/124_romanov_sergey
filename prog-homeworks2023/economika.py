n=int(input("Введите количество моментов времени"))
n1=n
r=n
r1=n
k=0
s=[]
d=[]
while r>0:
    print("Введите значение в ", r, " период времени")
    s.append(int(input()))
    r-=1
while r1>0:
    print("Введите значение в ", r1, " период времени")
    d.append(int(input()))
    r1-=1
for i in range(0, n):
        if s[i]==d[i]:
            k+=1
print(k)

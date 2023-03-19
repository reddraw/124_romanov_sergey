
x=int(input("Введите число, на которое будете делить"))
n=int(input("Введите количество чисел в последовательности"))
f=n+1
k=1
sum=0
while n>0:
    print("Введите" ,str(f-n), "число из последовательности")
    sum+=int(input())
    n-=1
def magic(sum, x):
    if sum%x==0:
        return True
    else:
        return False
otvet=magic(sum,x)
print(otvet)

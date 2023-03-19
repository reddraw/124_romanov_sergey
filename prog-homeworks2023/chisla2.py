a=float(input("Введите первое число"))
b=float(input("Введите второе число"))
c=a+b
eps=0.01
if a>b:
    eps=0.01*a
else:
    eps=0.01*b
def eqv(a,b,c):
    if abs((a+b)-c)<eps:
        print(a+b)
        print(c)
        return True
    else:
        return False
otvet=eqv(a,b,c)
print(otvet)
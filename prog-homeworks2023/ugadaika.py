import random
x=random.randint(1,101)
otvet=0
n=1
print("Введите имя пользователя")
name=str(input())
filename=str(name)+".txt"
result=''
while x!=otvet:
    print("Компьютер загадал число, введите ваше предположение")
    otvet=int(input())
    if x>otvet:
        print("Ваше число меньше загаданного")
        n+=1
    elif x<otvet:
        print("Ваше число больше загаданного")
        n+=1
    else:
        print("Поздравляю, вы угадали число")
        result=str(name)+" "+"прошёл игру за"+" "+str(n)+" попыток(ки)"
        file=open(filename, "w+")
        file.write(str(result))

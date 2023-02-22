import math
import requests
import datetime
import time
def sila(massa,g,mz,r):
    f=(massa*mz*g)/math.pow(r,2)
    return f
r=str()
g = 6.6743*math.pow(10, -11)
mz = 5.97600*math.pow(10, 24)
n = 0
massa = 420*math.pow(10, 3)
now=datetime.datetime.now()
now=str(now)
god=int(now[0]+now[1]+now[2]+now[3])
mont=int(now[5]+now[6])
day=int(now[8]+now[9])
chas=int(now[11]+now[12])
k = str()
print("Что вам нужно? 1. Гравитационную силу между Землёй и МКС в 12:00 по МСК этого дня. 2. Гравитационная сила Земли с другим небесным телом. (отправьте нужную цифру в консоль)")
k = str(input())
if k == "1":
    if int(chas) < 12:
        timestamp = datetime.datetime(god, mont, day - 1, 12)
        timestamp = time.mktime(timestamp.timetuple())
    elif int(chas) > 12:
        timestamp = datetime.datetime(god, mont, day, 12)
        timestamp = time.mktime(timestamp.timetuple())
    timestamp = str(timestamp)
    Response = requests.get("https://api.wheretheiss.at/v1/satellites/25544/positions?timestamps=" + timestamp)
    iss = Response.json()
    iss = str(iss)
    for i in range(0, len(iss) - 2):
        if iss[i] + iss[i + 1] + iss[i + 2] == "alt":
            for j in range(11, 17):
                r = r + iss[i + j]
    print(float(r))
    r = float(r) + 6371
    #f = (mz * massa * g) / math.pow(r, 2)
    f = sila(massa, g, mz, r)
    while f > 10:
        f /= 10
        n += 1
    print("Гравитационная сила МКС к Земле в 12:00 по МСК была равна", f, "* 10 ^", n - 6, "Ньютонов")
elif k == "2":
    print("Введите название небесного тела")
    nazv = str(input())
    print("Введите массу небесного тела в кг, сначала число, потом степень 10, в кг")
    k = float(input())
    print("Теперь введите степень 10")
    des = int(input())
    massa = k * math.pow(10, des)
    print("Введите расстояние от небесного тела до земли, сначала число, потом степень 10, в км")
    k = float(input())
    print("Теперь введите степень 10")
    des = int(input())
    r = k*math.pow(10, des)
    #f = (g * massa * mz) / math.pow(r, 2)
    f=sila(massa,g,mz,r)

    while f > 10:
        f/=10
        n += 1
    print("Гравитационная сила небесного тела", nazv, "к Земле равна", f, "*10^", n-6, "Ньютонов")
else:
    print("Неправильное значение, перезапустите консоль и больше так не делайте")
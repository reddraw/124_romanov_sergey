x=float(input("Введите количество денег Алисы"))
y=float(input("Введите количество денег Боба"))
z=float(input("Введите количество денег Чарли"))
cost=float(input("Введите стоимость подписки"))
ab=abs(cost-(x+y))
az=abs(cost-(x+z))
bz=abs(cost-(y+z))
otvet=str()
def tsena(ab,az,bz,cost,x,y,z):
    if ab<az and ab<bz and x+y>cost:
        return "Алиса и Боб"
    elif az<ab and az<bz and x+z>cost:
        return "Алиса и Чарли"
    elif bz<ab and bz<az and y+z>cost:
        return "Чарли и Боб"
print(tsena(ab,az,bz,cost,x,y,z))
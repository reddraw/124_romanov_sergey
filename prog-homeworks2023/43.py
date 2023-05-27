import requests
import urllib
import bs4

#god=input(("Введите год своего рождения"))
#month=input(("Введите месяц своего рождения"))
nomermonth=0
facts=str()
fact=str()
#spisok=["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
#for i in range(1,len(spisok)):
    #if month.lower()==spisok[i]:
        #nomermonth=i+1
#file=open(str(nomermonth)+"."+str(god)+".txt", 'w')
wikilink = "https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F%3A%D0%A1%D0%B5%D0%BD%D1%82%D1%8F%D0%B1%D1%80%D1%8C_2004_%D0%B3%D0%BE%D0%B4%D0%B0"
page=str(requests.get(wikilink).text)
print(type(page))
startpoint=page.find("mw-category mw-category-columns")
endpoint=page.find(">Источник")
for i in range(startpoint, endpoint):
    if page[i]+page[i+1]+page[i+2]+page[i+3]+page[i+4]=="title":
        j=i+7
        while page[j]!='"':
            fact+=page[j]
            j+=1
        if page[j]=='"':
            facts=facts+";"+fact
            fact=str()
print(facts)

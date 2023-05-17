import requests
import urllib
god=input(("Введите год своего рождения"))
month=input(("Введите месяц своего рождения"))
nomermonth=0
facts=str()
spisok=["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
for i in range(1,len(spisok)):
    if month.lower()==spisok[i]:
        nomermonth=i+1
file=open(str(nomermonth)+"."+str(god)+".txt", 'w')
wikilink = "https://ru.wikipedia.org/wiki/" + urllib.parse.quote("Категория:" + month + "_" + god + "_года")
print(wikilink)
#print(wikilink)
#def season_events(month, god, facts):
    #wikilink = "https://ru.wikipedia.org/wiki/" + urllib.parse.quote("Категория:" + month + "_" + god + "_года")
    #response=requests.get(wikilink)
    #for i in range(0,response):
        #if range[i]+range[i+1]+range[i+2]=="<h2>":
           # while range[i]+range[i+1]+range[i+2]+range[i+3]+range[i+4]!="mw-navigation":
               # kal+=range[i]
        #if



    #file.write("Вы родились в месяце " + month + " в " + "году, события, которые произошли в этом году:" + str(facts))



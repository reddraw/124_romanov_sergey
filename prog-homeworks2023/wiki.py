import requests
import urllib
month=input("Напишите месяц вашего рождения")
god=input("Напишите год вашего рождения")
nomermonth=int()
spisok=["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
print(len(spisok))
for i in range(1,len(spisok)):
    if month.lower()==spisok[i]:
        nomermonth=i+1
print(nomermonth)
wikilink="https://ru.wikipedia.org/wiki/"+urllib.parse.quote("Категория:"+month+"_"+god+"_года")
print(wikilink)
def season_events(number_of_month, year, short_page=None):
    file = open(month+ '(' + str(year) + ').txt', 'w')
    file.write("Вы родились в месяце "+str(month)+" в "+str(god)+" году, события, которые произошли в этот год и этот же месяц:" + str(fact) )
    counter=5
    response=requests.get("https://ru.wikipedia.org/wiki/"+urllib.parse.quote("Категория:"+month+"_"+god+"_года"),)
    page=response.text
    for i in range(page.find("<h2>Страницы в категории «Сентябрь 2004 года»</h2>"), page.find("<div class="printfooter" data-nosnippet="">Источник")):
        short_page+=i
    for j in range(0, len(short_page)-3):
        if short_page[i]+short_page[i+1]+short_page[i+2]+short_page[i+3]=="title":


print(season_events(month, god))

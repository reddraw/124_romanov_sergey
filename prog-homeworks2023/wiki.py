import requests
import urllib
month=input("Напишите месяц вашего рождения")
god=input("Напишите год вашего рождения")
facts=str()
def season_events(month, god,facts):
    page=requests.get("https://ru.wikipedia.org/wiki/"+urllib.parse.quote("Категория:"+month+"_"+god+"_года")).text
    page = str(page)
    startpoint = page.find("mw-category mw-category-columns")
    endpoint = page.find(">Источник")
    for i in range(startpoint, endpoint):
        fact = str()
        if page[i] + page[i + 1] + page[i + 2] + page[i + 3] + page[i + 4] == "title":
            j = i + 7
            while page[j] != '"':
                fact += page[j]
                j += 1
            facts = facts + fact+";"
            fact = str()
    file = open(month + '(' + str(god) + ').txt', 'w')
    file.write("Вы родились в месяце " + str(month) + " в " + str(god) + " году, события, которые произошли в этот год и этот же месяц:" + str(facts))
season_events(month,god,facts)

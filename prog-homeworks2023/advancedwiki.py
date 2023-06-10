import requests
import urllib
import re
day=input("Напишите день")
month=input("Напишите месяц")
facts=str()
factsrusdigit="Факты на русском языке(с цифрами):"
factsendigit="Факты на английском языке(с цифрами):"
factsmixed="Остальные факты:"
factsrus="Факты на русском языке(без скобок и цифр):"
if month.lower=="август" or month.lower=="март":
    month=month+"а"
else:
    month = month.rstrip(month[-1])
    month=month+"я"
page=requests.get("https://ru.wikipedia.org/wiki/"+urllib.parse.quote("Категория:События_"+str(day)+"_"+str(month))).text
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
        countcifr=0
        for k in range(0, len(fact)):
            if fact[k].isdigit():
                countcifr+=1
        if countcifr>0:
            proverka=bool(re.search('[а-яА-Я]', fact))
            if proverka:
                proverka=bool(bool(re.search('[a-zA-Z]', fact)))
                if proverka:
                    factsmixed=factsmixed+str(fact)+";"
                else:
                    factsrusdigit=factsrusdigit+str(fact)+";"
            else:
                factsendigit=factsendigit+str(fact)+";"
        else:
            if fact.count("(")>0:
                factsmixed=factsmixed+str(fact)+";"
            else:
                factsrus=factsrus+str(fact)+";"
facts=factsrus+factsendigit+factsmixed+factsrusdigit
file = open(day + '.' + str(month) + '.txt', 'w')
file.write(str(facts))
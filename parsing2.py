
def strr(abc):

    abc = list(abc)
    n = abc.count("\n")
    t = abc.count("\t")
    for i in range(n):
        abc.remove("\n")
    for j in range(t):
        abc.remove("\t") 
    abc = "".join(abc)
    return abc

def inttt(abc):

    abc = list(abc)
    for v in abc:
        if v == "\n":
            abc.remove("\n")

    for v1 in abc:    
        if v1 == ('\t'):
            abc.remove('\t')

    for v2 in abc:
        if v2 == "\xa0":
            abc.remove("\xa0")

    for v3 in abc:
        if v3 == ('z'):
            abc.remove('z')

    for v4 in abc:
        if v4 == "ł":
            abc.remove("ł")
    abc = "".join(abc)
    return abc



import mysql.connector
import requests
from bs4 import BeautifulSoup

dost = []
wart = []
#strona = requests.get("https://www.euro.com.pl/telewizory-led-lcd-plazmowe.bhtml#fromKeyword=telewizor")
strona = requests.get("https://www.euro.com.pl/konsole-playstation-5.bhtml?link=search#fromKeyword=playstation%205")

soup = BeautifulSoup(strona.text, "lxml")
body = soup.body
tytul = body.find('h2', {'class': 'product-name'}) 
tytul = tytul.a.string
tytul = str(tytul) #tytuł
tytul = strr(tytul)
cena = body.find('div', {'class': 'price-normal selenium-price-normal'})

cena = cena.text #cena
cena = inttt(cena)

wartosci = []
wartosci = body.find_all("span", {"class": "attribute-value"})
for x in wartosci: #wartości
    c = x.text
    wart.append(c)

wart4 = wart.pop()
wart4 = strr(wart4)
wart3 = wart.pop()
wart3 = strr(wart3)
wart2 = wart.pop()
wart2 = strr(wart2)
wart1 = wart.pop()
wart1 = strr(wart1)

dostawa = body.find_all("span", {"class" : "delivery-message"})
for i in dostawa: #dostawa
    b = i.text
    dost.append(b)
totu = dost.pop()
totu = strr(totu)



print("tytuł: ", tytul, "cena: ", cena, "dostawa: ", totu, "Wartosci: ", wart1, wart2, wart3, wart4)


idoferty = ("NULL")
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="ksiegarnia"
)

mycursor = mydb.cursor()

sql = ("INSERT INTO ps5 VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
val = (idoferty, tytul, cena, totu, wart1, wart2, wart3, wart4)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "wiersz dodany.")

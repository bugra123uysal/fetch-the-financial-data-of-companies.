from bs4 import BeautifulSoup
import requests



urll="https://www.kap.org.tr/tr/sirket-finansal-bilgileri/4028e4a140f2ed720140f37f139c01bc"

aa=requests.get(urll)
bb=aa.content
cc=BeautifulSoup(bb,"html.parser")

""" yıl """
dd=cc.find_all("div", class_="comp-cell-row-div vtable infoColumn compareItemsHeader")

""" tablo niteliği """
ff=cc.find_all("div", class_="comp-cell-row-div vtable itemsColumn")

""" 2024  son yıl verisi sayı almak """
gg=cc.find_all("div", class_="comp-cell-row-div vtable itemsColumn")




""" verileri yazdırma """

for yıl,tablo,sayı in zip (dd,ff,gg):
    print(f"{yıl.text.strip()}-- {tablo.text.strip()}={sayı.text.strip()} ")



from bs4 import BeautifulSoup as bs
import http.client as hc

conn = hc.HTTPSConnection("cvc.cervantes.es")
conn.request("GET", "/lengua/refranero/listado.aspx")

resp = conn.getresponse()

print(resp.read())
print(resp.status)

soup = bs(resp.read(), "html.parser")

def getParemia ():
    pass

def getAllParemia ():
    pass

soup.find()

"""
dir() - le pasas un object y te devuelve la estructura interna del objeto, variable y métodos
type() - le pasas un object y te devuelve el tipo del objeto
"""


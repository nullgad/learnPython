import requests
import urllib
import hashlib
from bs4 import BeautifulSoup


print("\n===================================")
print("\n        Emdee five for life        ")
print("\n===================================")
print("\n                 HTB               ")
print("\n===================================")


link = input("\n \n Enter the url : ")
port = input("\n Enter the Port : ")
url = "http://"+link+":"+port
sess=requests.session()

req = sess.get(url).text

beau = BeautifulSoup(req, 'lxml')
has = beau.h3.text


raw_hash = hashlib.md5(has.encode('utf-8')).hexdigest()

pos = sess.post(url, data={'hash':raw_hash}).text

beau1 = BeautifulSoup(pos, 'lxml')
flag = beau1.p.text
print("\n===================================")
print("\n            And the Flag is        ")
print("\n           " +flag+"               ")
print("\n===================================")
#
#  ==================================================================










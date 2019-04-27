import os
from requests import get
from bs4 import BeautifulSoup

def clear():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

clear()
asci = """  

 _____           _            _        _ _                 
|_   _|         | |          | |      | | |                
  | |  _ __  ___| |_ __ _ ___| |_ __ _| | | _____ _ __ ___ 
  | | | '_ \/ __| __/ _` / __| __/ _` | | |/ / _ \ '__/ __|
 _| |_| | | \__ \ || (_| \__ \ || (_| | |   <  __/ |  \__ \
|_____|_| |_|___/\__\__,_|___/\__\__,_|_|_|\_\___|_|  |___/
                                                           
by Nor Ahmad

"""
print (asci)
uIG = input('Masukkan Username ig : ')
url = get("https://insta-stalker.com/profile/" + uIG)

soup = BeautifulSoup(url.text, 'html.parser')
name = soup.find('h1',{'style':'margin-bottom: 0; font-size: 22px; font-weight: 600;'})
des = soup.find('p',{'style':'margin-top: 0; margin-bottom: 0; color: #212121;'})
info = soup.find('div',{'class':'profile-info'})
si = soup.find('a',{'id':'instagram-story-count'})
postingan = soup.find('p',{'style':'max-height: 137px; overflow: hidden;'})
try:
  nama = name.text.rstrip().lstrip()
  deskrip = des.text.rstrip().lstrip()
  inpo = info.text.rstrip().lstrip()
  story = si.text.rstrip().lstrip()
  post = postingan.text.rstrip().lstrip()
except:
  print('Ada yang salah atau error')
print ('Username :',uIG)
print ('Link : https://www.instagram.com'+uIG)
try:
  print ('Nama :'+nama)
  print ('Deskripsi :'+deskrip)
  print (inpo)
  print ('Jumlah Story :'+story)
  print ('Postingan terbaru kata-kata:'+post)
except:
  exit

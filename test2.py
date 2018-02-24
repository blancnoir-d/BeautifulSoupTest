from bs4 import BeautifulSoup
import requests

req = requests.get('https://www.naver.com')
html = req.text

soup = BeautifulSoup(html,'html.parser')

#div중 class명이 _PM_... 인걸 찾기 
find = soup.find_all("div","header_info _PM_timesquare_info")
print(find)


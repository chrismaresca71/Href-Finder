import urllib3
from bs4 import BeautifulSoup


for x in range(7):
    http = urllib3.PoolManager()
    if x == 0:
        r = http.request('GET', 'http://py4e-data.dr-chuck.net/known_by_Khai.html')
    else:
        r = http.request('GET', str(lst[17]))
    soup = BeautifulSoup(r.data, 'html.parser')
    lst = []
    names = []
    links = soup.find_all('a')
    for link in links:
        lst.append(link.get('href'))
        names.append(link.text)

print(names[17])
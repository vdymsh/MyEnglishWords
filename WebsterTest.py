from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

word = input("word: ").strip().lower()

resp = urlopen(r"https://www.merriam-webster.com/dictionary/" + word)   # скачиваем файл
html = resp.read().decode('utf8') # считываем содержимое
with open(r"data\webster_" + word + ".html", 'w', encoding="utf-8") as f:
    f.write(html)

# soup = BeautifulSoup(html, 'html.parser') # делаем суп
# table = soup.find('table', attrs = {'class' : 'wikitable sortable'})
# cnt = 0
# for tr in soup.find_all('tr'):
#     cnt += 1
#     for td in tr.find_all(['td', 'th']):
#         cnt *= 2
# print(cnt)

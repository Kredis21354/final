import requests
from bs4 import BeautifulSoup

URL = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

data = requests.get(URL).text

soup = BeautifulSoup(data, features="html.parser")

movies = soup.find_all("td", {"class":"titleColumn"})

for f in movies:
  print(f.getText())

movies = soup.find_all("td", {"class":"ratingColumn imdbRating"})

for f in movies:
  print(f.getText())
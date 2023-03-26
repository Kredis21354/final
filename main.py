import requests
from bs4 import BeautifulSoup

URL = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

data = requests.get(URL).text

soup = BeautifulSoup(data, features="html.parser")

movies = soup.find_all("td", {"class":"titleColumn"})

for f in movies[0:1]:
  print(f.getText())

movies = soup.find_all("td", {"class":"ratingColumn imdbRating"})

for f in movies[0:1]:
  print(f.getText())

movies = soup.find_all("td", {"class":"titleColumn"})

for f in movies[1:2]:
  print(f.getText())

movies = soup.find_all("td", {"class":"ratingColumn imdbRating"})

for f in movies[1:2]:
  print(f.getText())

movies = soup.find_all("td", {"class":"titleColumn"})

for f in movies[2:3]:
  print(f.getText())

movies = soup.find_all("td", {"class":"ratingColumn imdbRating"})

for f in movies[2:3]:
  print(f.getText())

movies = soup.find_all("td", {"class":"titleColumn"})

for f in movies[3:4]:
  print(f.getText())

movies = soup.find_all("td", {"class":"ratingColumn imdbRating"})

for f in movies[3:4]:
  print(f.getText())

movies = soup.find_all("td", {"class":"titleColumn"})

for f in movies[4:5]:
  print(f.getText())

movies = soup.find_all("td", {"class":"ratingColumn imdbRating"})

for f in movies[4:5]:
  print(f.getText())

movies = soup.find_all("td", {"class":"titleColumn"})

for f in movies[5:6]:
  print(f.getText())

movies = soup.find_all("td", {"class":"ratingColumn imdbRating"})

for f in movies[5:6]:
  print(f.getText())

movies = soup.find_all("td", {"class":"titleColumn"})

for f in movies[6:7]:
  print(f.getText())

movies = soup.find_all("td", {"class":"ratingColumn imdbRating"})

for f in movies[6:7]:
  print(f.getText())

movies = soup.find_all("td", {"class":"titleColumn"})

for f in movies[7:8]:
  print(f.getText())

movies = soup.find_all("td", {"class":"ratingColumn imdbRating"})

for f in movies[7:8]:
  print(f.getText())

movies = soup.find_all("td", {"class":"titleColumn"})

for f in movies[8:9]:
  print(f.getText())

movies = soup.find_all("td", {"class":"ratingColumn imdbRating"})

for f in movies[8:9]:
  print(f.getText())

movies = soup.find_all("td", {"class":"titleColumn"})

for f in movies[9:10]:
  print(f.getText())

movies = soup.find_all("td", {"class":"ratingColumn imdbRating"})

for f in movies[9:10]:
  print(f.getText())
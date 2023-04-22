import bs4
import requests

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
soup = bs4.BeautifulSoup(requests.get(url).text, "lxml")
soup = [ a.getText() for a in soup.find_all("h3", class_ = "title") ]

with open("top-movies.txt", "w") as file:
    for a in range(len(soup) - 1, -1, -1):
        file.write(soup[a]+'\n')

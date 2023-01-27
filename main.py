from bs4 import BeautifulSoup
import requests

# Get info from the website html
response = requests.get("https://news.ycombinator.com/")
yc = response.text
soup = BeautifulSoup(yc, "html.parser")
titles = soup.find_all("span", class_="titleline")
rank = soup.find_all("span", class_="score")
links = soup.find_all("a", href=True)

# List comprehension that gets the info from the website into a list
titles = [tag.getText() for tag in titles]
scores = [int(rank[index].getText().split()[0]) for index in range(len(rank))]
sources = [links[i]["href"] for i in range(len(links)) if "http" in links[i]["href"]]

# Find index of highest number
max = scores.index(max(scores))

# Print title and link of post with the highest score
print(scores[max],titles[max], sources[max+1])

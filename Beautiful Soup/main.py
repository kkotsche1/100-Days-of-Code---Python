from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_html = response.text

soup = BeautifulSoup(yc_html, "html.parser")
td_link = soup.find_all(name="a", class_="titlelink")
td_upvote = soup.find_all(name="span", class_="score")
article_text=[]
article_link=[]
article_score=[]


for article in td_link:

    article_text.append(article.get_text())
    article_link.append(article.get("href"))


for score in td_upvote:

    score = score.get_text()
    split_score = score.split(" ")
    article_score.append(int(split_score[0]))

highest_score = max(article_score)
largest_index = article_score.index(highest_score)



print(article_text)
print(article_link)
print(article_score)


print(article_text[largest_index])
print(article_link[largest_index])
print(article_score[largest_index])



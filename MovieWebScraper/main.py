import requests
from bs4 import BeautifulSoup



data = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
data = data.text

soup = BeautifulSoup(data, "html.parser")
movie_data = soup.find_all("h3")

movies = [movie.get_text( )for movie in movie_data]

list_length = len(movies)

flipped_list =[]

while list_length >=1:
    flipped_list.append(movies[list_length-1])
    list_length -=1


with open("movies.txt", "w") as file:
    for movie in flipped_list:
        file.write(movie)
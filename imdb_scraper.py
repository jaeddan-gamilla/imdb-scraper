import requests
import sys
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

BASE_URL = 'https://www.imdb.com/'


def get_genre_link():
    url = 'https://www.imdb.com/interest/all/'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    genres = soup.find_all('div', class_="ipc-slate-card__title-text ipc-slate-card__title-text--clamp-1")
    genre_link_extensions = soup.find_all('a', class_='ipc-slate-card__title ipc-slate-card__title--clickable sc-c5922af5-2 fhgilD')

    link_map = {}
    for i in range(len(genres)):
        link_map[genres[i].text] = BASE_URL + genre_link_extensions[i].get('href')

    return link_map


def get_top_movies(genre_url):
    response = requests.get(genre_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    movie_titles = soup.find_all('a', class_="ipc-poster-card__title ipc-poster-card__title--clamp-2 ipc-poster-card__title--clickable")

    top_movies = []
    for movie in movie_titles:
        top_movies.append(movie.text)
    
    return top_movies


def direct_movie_url(genre_url, selected_movie, movies):
    response = requests.get(genre_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    movie_link_extensions = soup.find_all('a', class_="ipc-lockup-overlay ipc-focusable")

    link_map = {}

    num_movies = min(len(movies), len(movie_link_extensions))

    for i in range(num_movies):  # Avoid IndexError
        link_map[movies[i]] = BASE_URL + movie_link_extensions[i].get('href')

    if selected_movie in link_map:
        return link_map[selected_movie]
    else:
        print('Invalid Movie Selected!')
        sys.exit(2)



def main(num_genres_to_display=None, selected_genre=None, selected_movie=None):
    link_map = get_genre_link()
    
    if num_genres_to_display is None:
        num_genres_to_display = input('How many genres are you interested in? (1 - 50): ')
        num_genres_to_display = int(num_genres_to_display)

    if not (1 <= num_genres_to_display <= 50):
        print('Please pick a number in the range 1 - 50!')
        exit(2)

    print("")
    
    if selected_genre is None:
        print('Available Genres:' + "")
        genres = list(link_map.keys())
        for i in range(int(num_genres_to_display)):
            print(genres[i])
    
        print("")
        selected_genre = input('Select a genre above: ')
        print("")

    genre_url = link_map.get(selected_genre)
    if genre_url is None:
        print('Invalid Genre Selected!')
        exit(2)
    else:
        movies = get_top_movies(genre_url)
        k = 1
        print('Top 10 trending in ' + selected_genre + ' movies:' + "")
        while (k < 11):
            print(str(k) + '. ' + movies[k - 1])
            k += 1
    
    print("")
    if selected_movie is None:
        selected_movie = input('Type in a movie of your choice to receive the direct URL!: ')
    
    selected_movie_url = direct_movie_url(genre_url, selected_movie, movies)

    print("")
    print('Here is your URL! Enjoy watching ' + selected_movie + "!" + "")
    print(selected_movie_url)


if __name__ == "__main__":
    main()
    

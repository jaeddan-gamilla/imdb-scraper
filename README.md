# IMDb-scraper
A Python-based web scraper that uses BeautifulSoup to extract trending movies from IMDb based on user-selected genres

# Installation
You will need to install BeautifulSoup to run this code.
~~~
pip install bs4
~~~

# Usage Example
~~~
.../imdb-scraper.py
~~~

After running, you will receive three prompts, which you must answer verbatim.

First:

`How many genres are you interested in? (1 - 50):`



Next, you will input a genre from any of those provided. 

`Select a genre above:`



An example of the list of genres you would see is below:

![image](https://github.com/user-attachments/assets/f3dd8c84-b2a9-4646-a818-0922b37d70b9)



After selecting a genre, the top 10 trending movies in that category are shown. These movies are not listed by ratings but rather by the first 10 movies that are scraped from the IMDb's movie genre HTML. The "Superhero" genre example is shown below:

![image](https://github.com/user-attachments/assets/55a7774b-0949-4fa9-91a1-a18ce3b413ae)



Lastly, you are given the prompt:



`Type in a movie of your choice to receive the direct URL!:`



Here, you must input a movie title as it is provided in the terminal. Typos will result in an exit of the code.

Once you input a movie title, you are given the exact IMBd URL link to the selected movie.


![image](https://github.com/user-attachments/assets/4c97bd46-5d42-4334-a925-560390700f1f)
![image](https://github.com/user-attachments/assets/92c8a7b2-6e45-4746-9ff9-d85f605a34a0)

As you can see above, the URL link provided in the command prompt led me directly to my desired movie.

# Testing
Upon a look through my `imdb_scraper.py` code, you will see there are three times where `exit(2)` occurs: When a number is given out of range 1-50 when asked for a number of genres, when an incorrect genre is provided, and when an incorrect movie title is provided. Please see the `test_imdb_scraper.py` file to see how I test it in `main()`.

# Inspiration
I found inspiration to create my first Python project based on Nishant Sahoo's post on Medium.
\
\
Link:
https://medium.com/@nishantsahoo/which-movie-should-i-watch-5c83a3c0f5b1





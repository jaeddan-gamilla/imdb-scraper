import unittest
import sys
from imdb_scraper import get_genre_link, direct_movie_url

#TESTS IMDB SCRAPER FOR ERRORS WHEN NECESSARY

class TestIMDBScraper(unittest.TestCase):

    def test_invalid_genre_number_0(self):
        """Test selecting '0' as the number of genres (out of range)"""
        num_genres_to_display = 0  # Invalid input (should be between 1-50)

        with self.assertRaises(SystemExit) as cm:
            if num_genres_to_display > 50 or num_genres_to_display < 1:
                print('Please pick a number in the range 1 - 50!')
                sys.exit(2)  # Expected exit condition

        self.assertEqual(cm.exception.code, 2)  # Ensure exit(2) was called

    def test_invalid_genre_number_51(self):
        """Test selecting '51' as the number of genres (out of range)"""
        num_genres_to_display = 51  # Invalid input (should be between 1-50)

        with self.assertRaises(SystemExit) as cm:
            if num_genres_to_display > 50 or num_genres_to_display < 1:
                print('Please pick a number in the range 1 - 50!')
                sys.exit(2)  # Expected exit condition

        self.assertEqual(cm.exception.code, 2)  # Ensure exit(2) was called

    def test_invalid_genre_selection(self):
        """Test selecting an invalid genre ('Funny Movies')"""
        link_map = {"Action": "https://www.imdb.com/action/", "Comedy": "https://www.imdb.com/comedy/"}
        selected_genre = "Funny Movies"  # Invalid genre

        with self.assertRaises(SystemExit) as cm:
            genre_url = link_map.get(selected_genre)
            if genre_url is None:
                print('Invalid Genre Selected!')
                sys.exit(2)  # Expected exit condition

        self.assertEqual(cm.exception.code, 2)  # Ensure exit(2) was called

    def test_invalid_movie_selection(self):
        """Test selecting an invalid movie ('Spongebob Squarepants')"""
        movies = ["Movie A", "Movie B", "Movie C"]
        genre_url = "https://www.imdb.com/action/"  # Example genre URL
        selected_movie = "Spongebob Squarepants"  # Invalid movie name

        with self.assertRaises(SystemExit) as cm:
            movie_url = direct_movie_url(genre_url, selected_movie, movies)

        self.assertEqual(cm.exception.code, 2)  # Ensure exit(2) was called

if __name__ == "__main__":
    unittest.main()

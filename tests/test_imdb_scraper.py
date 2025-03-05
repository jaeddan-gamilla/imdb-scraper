import unittest
from imdb_scraper import main
from io import StringIO
import sys

class TestIMDBScraper(unittest.TestCase):

    def test_invalid_genre_number_0(self):
        with self.assertRaises(SystemExit) as cm:
            main(num_genres_to_display=0)  # Run script with invalid input
        self.assertEqual(cm.exception.code, 2)  # Ensure exit(2) was triggered

    def test_invalid_genre_number_51(self):
        with self.assertRaises(SystemExit) as cm:
            main(num_genres_to_display=51)
        self.assertEqual(cm.exception.code, 2)

    def test_invalid_genre_selection(self):
        with self.assertRaises(SystemExit) as cm:
            main(num_genres_to_display=1, selected_genre="Funny Movies")
        self.assertEqual(cm.exception.code, 2)

    def test_invalid_movie_selection(self):
        with self.assertRaises(SystemExit) as cm:
            main(num_genres_to_display=1, selected_genre="Action", selected_movie="Spongebob Squarepants")
        self.assertEqual(cm.exception.code, 2)

    def test_valid_movie_selection(self):

        captured_output = StringIO()
        sys.stdout = captured_output

        try:
            main(num_genres_to_display=32, selected_genre="Sci-Fi", selected_movie="Interstellar")
        except SystemExit:
            self.fail("main() exited unexpectedly.")

        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()

        self.assertIn("https://www.imdb.com/", output, "Expected IMDb link not found in output.")


if __name__ == "__main__":
    unittest.main()


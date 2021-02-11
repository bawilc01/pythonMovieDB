# Movie Class example
import csv
from pip._vendor.distlib.compat import raw_input


class Movie:
    filename = 'movieList.csv'

    def __init__(self, title, rating, formatType):
        self.title = title
        self.rating = rating
        self.formatType = int(formatType)

    # def __str__(self):
    #     s = ["-----",
    #          f'Movie Title: {self.title}',
    #          f'Movie Rating: {self.rating}',
    #          f'Movie Type: {self.formatType}']
    #     return "\n".join(s)

    @classmethod
    def addMovie(cls):
        return cls(
            raw_input(f'Please enter a movie title: '),
            raw_input(f'Please enter a movie rating: '),
            int(raw_input(f'Please select from the following for movie type: \n'
                          f'1 - DVD \n'
                          f'2 - Bluray \n'
                          f'3 - Digital')),
        )

        fields = [self.title, self.rating, self.formatType]
        with (Movie.filename, 'a+') as f:
            writer = csv.writer(f)
            writer.writerow(fields)
            f.close()

    def viewMovieList(self):
        pass

    def removeMovie(self):
        pass


def main(logger):
    logger.info(f'Welcome to Movie List.')

    choice = input(f'Please enter the corresponding number for your choice: '
                   f'\n 1 - View List of Movies'
                   f'\n 2 - Add Movie'
                   f'\n 3 - Delete Movie'
                   f'\n Please type the number for your choice: ')

    logger.info(f'Great! Your choice is: {choice}')

    if choice == 2:
        movie = input(Movie.addMovie())
        logger.info(f'You entered {movie} to your database!')

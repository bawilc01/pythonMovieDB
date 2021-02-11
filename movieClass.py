# Movie Class example
import csv


class Movie:
    filename = 'movieList.csv'

    def __init__(self, title, rating, formatType):
        self.title = title
        self.rating = rating
        self.formatType = int(formatType)


    @classmethod
    def addMovie(cls):
        title = input(f'Please enter a movie title: ')
        rating = input(f'Please enter a movie rating: ')
        formatType = int(input(f'Please select from the following for movie type: \n'
                      f'1 - DVD \n'
                      f'2 - Bluray \n'
                      f'3 - Digital'))

        fields = [title, rating, formatType]
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

    if choice == 2:
        logger.info(f'Great! Your choice is: {choice}')
        movie = Movie()
        movie.addMovie()
        logger.info(f'You entered {movie} to your database!')

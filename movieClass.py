# Movie Class example
import csv


class Movie:
    filename = 'movieList.csv'

    def __init__(self, title, rating, formatType):
        self.title = title
        self.rating = rating
        self.formatType = int(formatType)

    def show_movie(self):
        return f'You have added {self.title}, {self.rating}, {self.formatType} to your database.'


    @classmethod
    def addMovie(self, logger):
        try:
            title = input(f'Please enter a movie title: ')
            rating = input(f'Please enter a movie rating: ')
            formatType = input(f'Please select for movie type: \n'
                          f'1 - DVD \n'
                          f'2 - Bluray \n'
                          f'3 - Digital')
            return self(title, rating, formatType)
        except:
            logger.info(f'Invalid info!')
            exit()


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

    if choice == str(2):
        logger.info(f'Great! Your choice is: {choice}')
        movie = Movie.addMovie(logger)
        movie.show_movie()
        logger.info(f'You entered {movie} to your database!')
        exit()
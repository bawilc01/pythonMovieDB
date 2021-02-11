# Movie Class example
import csv
import pandas as pd


class Movie:

    def __init__(self, title, rating, formatType):
        self.title = title
        self.rating = rating
        self.formatType = int(formatType)

    def show_movie(self, logger):
        m = {'Title': self.title, 'Rating': self.rating,
             'MovieType': str(self.formatType)}

        df = pd.DataFrame(m)

        print(df)

        # filename = 'movieList.csv'

        # with open(filename, 'a+', encoding='utf-8') as f:
        #     writer = csv.writer(f)
        #     for key, value in m.items():
        #         writer.writerow([key, value])
        logger.info(f'You have added {self.title}, {self.rating}, {self.formatType} to your database.')


    @classmethod
    def addMovie(self, logger):
        try:
            title = input(f'Please enter a movie title: ')
            rating = input(f'Please enter a movie rating: ')
            formatType = input(f'Please select for movie type: \n'
                          f'1 - DVD \n'
                          f'2 - Bluray \n'
                          f'3 - Digital \n')
            return self(title, rating, formatType)


        except:
            logger.info(f'Invalid info!')
            exit()



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
    choice = int(choice)

    if choice == 2:
        logger.info(f'Great! Your choice is: {choice}')
        movie = Movie.addMovie(logger)
        movie.show_movie(logger)
        exit()
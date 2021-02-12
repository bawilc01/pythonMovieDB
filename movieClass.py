# Movie Class example
import csv
import pandas as pd


class Movie:

    def __init__(self, title, rating, formatType):
        self.title = title
        self.rating = rating
        self.formatType = int(formatType)

    @classmethod
    def addMovie(self, logger):
        try:
            numberOfMovies = input(f'How many movies do you want to enter?\n')
            numberOfMovies = int(numberOfMovies)
            title = []
            rating = []
            formatType = []

            for i in range(numberOfMovies):
                t = input(f'Please enter a movie title: ')
                r = input(f'Please enter a movie rating: ')
                ft = input(f'Please select for movie type: \n'
                              f'1 - DVD \n'
                              f'2 - Bluray \n'
                              f'3 - Digital \n')
                title.append(t)
                rating.append(r)
                formatType.append(ft)

            filename = 'movieList.csv'
            m = {'Title': title, 'Rating': rating, 'MovieType': formatType}
            df = pd.DataFrame(m)
            df.to_csv(filename, mode='a+', header=False, index=False)
            print(df)

            #TODO need to do a split function with foreach loop
            logger.info(f'You entered {title}, {rating}, {formatType} to your database.')

        except:
            logger.info(f'Invalid info!')
            exit()


    def removeMovie(self):
        pass


def viewMovieList():
    filename = 'movieList.csv'
    data = pd.read_csv(filename)
    print(data)

def main(logger):
    logger.info(f'Welcome to Movie List.')

    choice = input(f'Please enter the corresponding number for your choice: '
                   f'\n 1 - View List of Movies'
                   f'\n 2 - Add Movie'
                   f'\n 3 - Delete Movie'
                   f'\n Please type the number for your choice: ')
    choice = int(choice)

    if choice == 1:
        logger.info(f'Great! Your choice is: {choice}')
        viewMovieList()
    elif choice == 2:
        logger.info(f'Great! Your choice is: {choice}')
        movie = Movie.addMovie(logger)
    else:
        logger.info('No delete function yet.')
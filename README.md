### Instructions:

1. Run this command to install dependencies stored in the requirements file:

    pip install -r requirements.txt (Python 2)

    pip3 install -r requirements.txt (Python 3)

2. Run the main.py file and follow instructions.

3. When adding movies, the movies are stored in a csv file called movieList.csv saved in the same folder as the .py files. 
   I'm ignoring it in the .gitignore for now.  
   Each entry is read into a pandas dataframe. New movies are appended to the csv. Open the file on your local machine if 
   you would like to see the csv that is acting as a "database".

I haven't figured out how to print the headers once and then only append the values. Right now, I have the headers set 
to False and manually typed 'Title, Rating, Movie Type' into the first row of my csv. It looks like
items are printed automatically to line #2 in the csv so typing header names doesn't seem to 
cause an issue.

### Files and Definitions
##### main.py

Only file that needs to run. It calls the main function in the movieClass.py file.


##### movieClass.py

Holds information about classes, methods and functions needed to add and view movies in database (csv file)

### Other Notes
 Since this is a very basic app put together very quickly for a demo, there are no exceptions caught at the moment. Some
 answers to questions might throw errors. For example, if you enter 'two' as the answer to "how many movies
 would you like to add", a value error would be thrown as it only accepts integer answers.
 
 I also have not done anything to print off enum items. For example, movie type is stored as an int depending
 on the type entered by the user. But I'm not printing the type 'DVD' into the pandas dataframe
 when formatType = 1. This is something that can be handled later.

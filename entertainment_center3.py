#import the movie class called "media3"
#import the module that will generate the website

import media3
import fresh_tomatoes2

# identify 6 instances of my favorite movies with the defined attributes
# the attributes include the movie title, box art URL (or poster URL), 
#    a YouTube link to the movie trailer, who stars in the movie, and the movie rating.
star_wars = media3.Movie("Star Wars","http://upload.wikimedia.org/wikipedia/fa/thumb/8/87/StarWarsMoviePoster1977.jpg/200px-StarWarsMoviePoster1977.jpg","https://www.youtube.com/watch?v=1g3_CFmnU7k", "Mark Hamill, Harrison Ford, Carrie Fisher, Peter Cushing, Alec Guiness", "PG")

its_complicated = media3.Movie("It's Complicated","http://upload.wikimedia.org/wikipedia/en/e/ee/Its_complicated_ver2.jpg","https://www.youtube.com/watch?v=kNDHiRb_XoU","Meryl Streep, Steve Martin and Alec Baldwin", "R")

goldfinger = media3.Movie("Goldfinger","http://upload.wikimedia.org/wikipedia/en/9/9a/Goldfinger_-_UK_cinema_poster.jpg","https://www.youtube.com/watch?v=KdQoSK9wibU", "Sean Connery, Honor Blackman, Gert Frobe", "PG")
the_lego_movie = media3.Movie("The Lego Movie","http://upload.wikimedia.org/wikipedia/en/1/10/The_Lego_Movie_poster.jpg", "https://www.youtube.com/watch?v=fZ_JOBCLF-I", "Chris Pratt, Will Ferrell, Elizabeth Banks", "PG")                              

truth_cats_dogs = media3.Movie("The Truth about Cats and Dogs","http://upload.wikimedia.org/wikipedia/en/1/1d/Truth_about_cats_and_dogs_movie_poster.jpg","https://www.youtube.com/watch?v=6nFJcAt-ktU","Janeane Garofalo, Uma Thurman, Ben Chaplin and Jamie Foxx", "PG-13")

thomas_crown = media3.Movie("The Thomas Crown Affair", "http://upload.wikimedia.org/wikipedia/en/6/66/Thomascrownposter1999.jpg", "https://www.youtube.com/watch?v=qDaYmYR2LXQ","Pierce Brosnan, Rene Russo and Denis Leary", "R")

#group all the movie instances together in one list
movies =[star_wars, its_complicated, goldfinger, the_lego_movie, truth_cats_dogs, thomas_crown]

#call on the module to create the website using the one list or argument containing the grouping of the movie instances
fresh_tomatoes2.open_movies_page(movies)




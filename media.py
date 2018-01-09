class Movie():
    def __init__(self, movie_title, movie_storyline, movie_image,
                 movie_trailer):
        """This function constructs an instance of Movie class for each movie.
        The arguments are assigned to the corresponding instand variabales.
        Args:
            movie_title(str):Holds the title of the movie
            movie_storyline(str):Holds the plot of the movie
            movie_image(str):Holds a url linked to the box art of the movie
            movie_trailer(str):Holds the url to the Youtube trailer video of the move
        Returns:
            Returns an instance of movies
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_image
        self.trailer_youtube_url = movie_trailer

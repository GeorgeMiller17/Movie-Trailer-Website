import media
import fresh_tomatoes


"""
Use instances of Moive class to store information of movies
"""
your_name = media.Movie("Your name",
                        '''Two strangers find themselves linked in a bizarre way.
                        When a connection forms,
                        will distance be the only thing to keep them apart''',
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BODRmZDVmNzUtZDA4ZC00NjhkLWI2M2UtN2M0ZDIzNDcxYThjL2ltYWdlXkEyXkFqcGdeQXVyNTk0MzMzODA@._V1_SY1000_SX675_AL_.jpg",
                        "https://www.youtube.com/watch?v=xU47nhruN-Q")


papurika = media.Movie("Papurika",
                        '''When a machine that allows therapists to enter their patients' dreams is stolen,
                        all Hell breaks loose. Only a young female therapist, Paprika, can stop it.''',
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMWM0M2RlZjktMTY0My00YTdjLTkzZTctYmZhYzhlY2Q1ZTgyXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,703,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=yn7U1KIGeuQ")


akira = media.Movie("Akira",
                    '''A secret military project endangers Neo-Tokyo
                    when it turns a biker gang member into a rampaging psychic psychopath
                    that only two teenagers and a group of psychics can stop.''',
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BOGJmNzU2ZTktYTY5YS00ODA4LWFkNWYtYjcwZDY1NzZiZGUxXkEyXkFqcGdeQXVyMzM4MjM0Nzg@._V1_SY1000_CR0,0,694,1000_AL_.jpg",
                    "https://www.youtube.com/watch?v=NCmVrn2gnRs")



tokyo_Goddofazazu = media.Movie("Tokyo Goddofazazu",
                                '''On Christmas Eve, three homeless people living on the streets of Tokyo
                                find a newborn baby among the trash and set out to find its parents.''',
                                "https://images-na.ssl-images-amazon.com/images/M/MV5BZmUyOTBkNjgtYjIzMi00ZTk1LWE4MDAtOWVmMzVhMzFjMTEwL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMzM4MjM0Nzg@._V1_.jpg",
                                "https://www.youtube.com/watch?v=vNGiL9UNONU")


summer_wars = media.Movie("Summer Wars",
                          '''A student tries to fix a problem he accidentally caused in OZ,
                          a digital world, while pretending to be the fiance of his friend
                          at her grandmother's 90th birthday.''',
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYyOTk3OTQzM15BMl5BanBnXkFtZTcwMjU4NDYyNA@@._V1_SY1000_CR0,0,681,1000_AL_.jpg",
                          "https://www.youtube.com/watch?v=IsLwVoZqEjk")


girl_who_leapt_through_time = media.Movie("The Girl Who Leapt Through Time",
                                          '''A high-school girl named Makoto acquires the power to travel back in time,
                                          and decides to use it for her own personal benefits.
                                          Little does she know that she is affecting the lives of others
                                          just as much as she is her own.''',
                                          "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA4MjE4NzE4NF5BMl5BanBnXkFtZTgwMjg1NDIxOTE@._V1_.jpg",
                                          "https://www.youtube.com/watch?v=eWnTeKEsDlU")

#use a list to store the instances of Movie class
movies = [your_name, papurika, akira,
          tokyo_Goddofazazu, summer_wars, girl_who_leapt_through_time]

#class fresh_tomatoes module to generate the html file
fresh_tomatoes.open_movies_page(movies)

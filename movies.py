# Movie object takes title, poster image, and youtube trailer inputs as strings
class Movie:
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

        
# Movie instances
fellowship_of_the_ring = Movie("LOTR: The Fellowship of the Ring",
                   "http://vignette3.wikia.nocookie.net/lotr/images/7/74/LOTRFOTRmovie.jpg/revision/latest?cb=20150203040819", # NOQA
                   "https://www.youtube.com/watch?v=Pki6jbSbXIY")

two_towers = Movie("LOTR: The Two Towers",
                   "https://upload.wikimedia.org/wikipedia/en/a/ad/Lord_of_the_Rings_-_The_Two_Towers.jpg", # NOQA
                   "https://www.youtube.com/watch?v=2dlRvAjU_RI")

return_of_the_king = Movie("LOTR: Return of the King",
                           "https://upload.wikimedia.org/wikipedia/en/9/9d/Lord_of_the_Rings_-_The_Return_of_the_King.jpg", # NOQA
                           "https://www.youtube.com/watch?v=r5X-hFf6Bwo")

                   
# List of all movie instances
movie_list = [fellowship_of_the_ring,
              two_towers,
              return_of_the_king]

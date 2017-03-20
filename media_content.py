import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "81 minutes", "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "G", "John Lasseter", "Animated")

avatar = media.Movie("Avatar", "161 Minutes",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                     "PG-13", "James Cameron", "Sci-Fi")

gladiator = media.Movie("Gladiator", "116 minutes", "https://www.youtube.com/watch?v=AxQajgTyLcM",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/8/8d/Gladiator_ver1.jpg/220px-Gladiator_ver1.jpg",
                        "R", "Ridley Scott", "Epic")


sons = media.Tv_Show("Sons of Anarchy", "47 minutes",
                             "https://www.youtube.com/watch?v=FXjbllOSUnQ",
                             "https://upload.wikimedia.org/wikipedia/en/7/7b/SOATitlecard.jpg",
                             "HBO", "Sunday 10pm")
old_house = media.Tv_Show("This Old House", "24 minutes",
                         "https://www.youtube.com/watch?v=TG0F7Qe4MzM",
                         "https://upload.wikimedia.org/wikipedia/en/thumb/5/5b/This_Old_House_%28logo%29.svg/250px-This_Old_House_%28logo%29.svg.png",
                          "PBS", "Sunday 10am")


# added a second array to handle TV Shows
movies = [toy_story, avatar, gladiator]
shows = [sons, old_house]

# This method creates the page and populates the media data
fresh_tomatoes.open_media_page(movies, shows)
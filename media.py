import webbrowser

# Create Parent class to hold shared variables
class Media:

    def __init__(self, mTtitle, mDuration, mTrailer, mImage):

        self.title = mTtitle
        self.duration = mDuration
        self.trailer = mTrailer
        self.img = mImage

    def Show_trailer(self):
        webbrowser.open(self.trailer)

# Create child classes to inherit Parent variable and method as well as specific data.

class Movie(Media):
    def __init__(self, mTitle, mDuration, mTrailer, mImage, mRating, mDirector, mGenre):
        Media.__init__(self, mTitle, mDuration, mTrailer, mImage)
        self.rating = mRating
        self.director = mDirector
        self.genre = mGenre

class Tv_Show(Media):
    def __init__(self, mTitle, mDuration, mTrailer, mImage, mChannel, mTime):
        Media.__init__(self, mTitle, mDuration, mTrailer, mImage)
        self.channel = mChannel
        self.time = mTime
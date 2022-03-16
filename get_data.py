import random
import requests

DriverTMDB = requests.get(
    "https://api.themoviedb.org/3/movie/64690?api_key=17084064f53176241a41dbed821dcea3&language=en-US"
)
DriverOT = DriverTMDB.json()["original_title"]
DriverTagline = DriverTMDB.json()["tagline"]
DriverOverview = DriverTMDB.json()["overview"]
DriverRatings = DriverTMDB.json()["vote_average"]
DriverPoster = "https://www.themoviedb.org/t/p/w780" + DriverTMDB.json()["poster_path"]
DriverRevenue = DriverTMDB.json()["revenue"]

DriverWiki = requests.get(
    "https://en.wikipedia.org/w/api.php?action=parse&format=json&page=Drive_(2011_film)&section=2"
)
DriverWikiParse = DriverWiki.json()["parse"]
links = DriverWikiParse["links"]
DriverCast = []
for a in links:
    x = a["*"]
    DriverCast.append(x)


AOTCTMBD = requests.get(
    "https://api.themoviedb.org/3/movie/1894?api_key=17084064f53176241a41dbed821dcea3&language=en-US"
)
AOTCOT = AOTCTMBD.json()["original_title"]
AOTCTagline = AOTCTMBD.json()["tagline"]
AOTCOverview = AOTCTMBD.json()["overview"]
AOTCRatings = AOTCTMBD.json()["vote_average"]
AOTCPoster = "https://www.themoviedb.org/t/p/w780" + AOTCTMBD.json()["poster_path"]
AOTCRevenue = AOTCTMBD.json()["revenue"]

AOTCWiki = requests.get(
    "https://en.wikipedia.org/w/api.php?action=parse&format=json&page=Star_Wars%3A_Episode_II_%E2%80%93_Attack_of_the_Clones&prop=text%7Ccategories%7Clinks%7Ctemplates%7Cimages%7Cexternallinks%7Csections%7Crevid%7Cdisplaytitle%7Ciwlinks%7Cproperties%7Cparsewarnings%7Cmodules&section=2"
)
AOTCWikiParse = AOTCWiki.json()["parse"]
links = AOTCWikiParse["links"]
AOTCCast = []
for a in links:
    x = a["*"]
    AOTCCast.append(x)

GreenMileTMDB = requests.get(
    "https://api.themoviedb.org/3/movie/497?api_key=17084064f53176241a41dbed821dcea3&language=en-US"
)
GreenMileOT = GreenMileTMDB.json()["original_title"]
GreenMileTagline = GreenMileTMDB.json()["tagline"]
GreenMileOverview = GreenMileTMDB.json()["overview"]
GreenMileRatings = GreenMileTMDB.json()["vote_average"]
GreenMilePoster = (
    "https://www.themoviedb.org/t/p/w780" + GreenMileTMDB.json()["poster_path"]
)
GreenMileRevenue = GreenMileTMDB.json()["revenue"]

GreenMileWiki = requests.get(
    "https://en.wikipedia.org/w/api.php?action=parse&format=json&page=The_Green_Mile_(film)&prop=text%7Ccategories%7Clinks%7Ctemplates%7Cimages%7Cexternallinks%7Csections%7Crevid%7Cdisplaytitle%7Ciwlinks%7Cproperties%7Cparsewarnings%7Cmodules&section=2"
)
GreenMileWikiParse = GreenMileWiki.json()["parse"]
links = GreenMileWikiParse["links"]
GreenMileCast = []
for a in links:
    x = a["*"]
    GreenMileCast.append(x)


class Movie(object):
    def __init__(
        self, originalTitle, tagline, overview, poster, cast, ratings, boxOffice
    ):
        self.originalTitle = originalTitle
        self.tageline = tagline
        self.overview = overview
        self.poster = poster
        self.cast = cast
        self.ratings = ratings
        self.boxOffice = boxOffice


Driver = Movie(
    DriverOT,
    DriverTagline,
    DriverOverview,
    DriverPoster,
    DriverCast,
    DriverRatings,
    DriverRevenue,
)

AOTC = Movie(
    AOTCOT, AOTCTagline, AOTCOverview, AOTCPoster, AOTCCast, AOTCRatings, AOTCRevenue
)

GreenMile = Movie(
    GreenMileOT,
    GreenMileTagline,
    GreenMileOverview,
    GreenMilePoster,
    GreenMileCast,
    GreenMileRatings,
    GreenMileRevenue,
)

Movies = [Driver, AOTC, GreenMile]


class Getmovie:
    x = random.randint(0, 2)
    Gettitle = Movies[x].originalTitle
    Gettagline = Movies[x].tageline
    Getoverview = Movies[x].overview
    Getposter = Movies[x].poster
    Getcast = Movies[x].cast
    Getratings = Movies[x].ratings
    Getrevenue = Movies[x].boxOffice

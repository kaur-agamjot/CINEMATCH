from flask import Flask, render_template, request

app = Flask(__name__)

movies = [
    # ACTION
    {
        "title": "Superman",
        "industry": "Hollywood",
        "genre": ["Action", "Adventure", "Sci-Fi"],
        "year": 2025,
        "description": "Superman discovers his identity while protecting humanity.",
        "poster": "https://image.tmdb.org/t/p/w500/ombsmhYUqR4qqOLOxAyr5V8hbyv.jpg"
    },
    {
        "title": "War 2",
        "industry": "Bollywood",
        "genre": ["Action", "Thriller"],
        "year": 2025,
        "description": "An action thriller involving a high-stakes mission.",
        "poster": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRKYFMMQztzJzt-Ve0-P3Islaz524aBYTz2oZ3MAd37sA&s=10"
    },
    {
        "title": "Jawan",
        "industry": "Bollywood",
        "genre": ["Action", "Thriller", "Drama"],
        "year": 2023,
        "description": "A high-energy action film about a man fighting injustice.",
        "poster": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRA1GB2GCr61TeYL7dUWVCh_QUgN5ks5G-IDtqW6bUQxQ&s=10"
    },
    {
        "title": "Pathaan",
        "industry": "Bollywood",
        "genre": ["Action", "Adventure", "Thriller"],
        "year": 2023,
        "description": "An Indian spy takes on a dangerous international mission.",
        "poster": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRqyLL_9MT44q33UWwYzdi6d-uIsmBIiThHUSOWn4-XhA&s=10"
    },
    {
        "title": "Mission: Impossible – The Final Reckoning",
        "industry": "Hollywood",
        "genre": ["Action", "Adventure", "Thriller"],
        "year": 2025,
        "description": "Ethan Hunt faces another high-stakes global mission.",
        "poster": "https://image.tmdb.org/t/p/w500/NNxYkU70HPurnNCSiCjYAmacwm.jpg"
    },

    # ADVENTURE
    {
        "title": "F1: The Movie",
        "industry": "Hollywood",
        "genre": ["Sports", "Drama"],
        "year": 2025,
        "description": "A former racing driver returns to Formula One.",
        "poster": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSr2SgmDLkFhLGuF1CnP_xJv1stiKvK027DkN6m6wdqdg&s=10"
    },
    {
        "title": "Avatar: The Way of Water",
        "industry": "Hollywood",
        "genre": ["Adventure", "Sci-Fi", "Drama"],
        "year": 2022,
        "description": "The Sully family explores the oceans of Pandora.",
        "poster": "https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
    },
    {
        "title": "Dune: Part Two",
        "industry": "Hollywood",
        "genre": ["Adventure", "Sci-Fi", "Drama"],
        "year": 2024,
        "description": "Paul Atreides joins the Fremen on a journey across Arrakis.",
        "poster": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRylJUeDX0A3szgi45w98Mu_lnGQ20a5PErFHJsrPV9CA&s=10"
    },
    {
        "title": "Jumanji: Welcome to the Jungle",
        "industry": "Hollywood",
        "genre": ["Adventure", "Comedy", "Action"],
        "year": 2017,
        "description": "Four teenagers enter a mysterious video game world.",
        "poster": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS5m4YxC-uGuFn-U5xCdAHy3Z4kQWbsszJ7cOBRYXqyFw&s=10"
    },
    {
        "title": "Brahmastra",
        "industry": "Bollywood",
        "genre": ["Adventure", "Fantasy", "Action"],
        "year": 2022,
        "description": "A young man discovers a powerful connection to ancient forces.",
        "poster": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTLHibwtutNG2OvcPUAQvMTzv6qTK-xC151yuELvyMing&s=10"
    },

    # COMEDY
    {
        "title": "Hera Pheri",
        "industry": "Bollywood",
        "genre": ["Comedy"],
        "year": 2000,
        "description": "Three characters get caught in a series of hilarious misunderstandings.",
        "poster": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQVdgGRXvR86czhqTT1vLFn41jaUUB3TNiaBr3DJf1FNA&s=10"
    },
    {
        "title": "3 Idiots",
        "industry": "Bollywood",
        "genre": ["Comedy", "Drama"],
        "year": 2009,
        "description": "Three friends navigate college, friendship and life's expectations.",
        "poster": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQSwknTty0Jpl5V4wQmKnVNuuwZgdrcH5nfoxlrn2zp5g&s=10"
    },
    {
        "title": "Munna Bhai M.B.B.S.",
        "industry": "Bollywood",
        "genre": ["Comedy", "Drama"],
        "year": 2003,
        "description": "A lovable gangster tries to become a doctor to impress his family.",
        "poster": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQb-S8mWtqPE-E42YG0t4D8vbw814hqWtQeRg-VVF2f8g&s=10"
    },
    {
        "title": "The Hangover",
        "industry": "Hollywood",
        "genre": ["Comedy"],
        "year": 2009,
        "description": "Friends try to piece together a chaotic night in Las Vegas.",
        "poster": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSz8Pg9pR1ku05lYsHHb3wPjy-NQvuQg2ZvV_PjPGgP6w&s=10"
    },
    {
        "title": "Home Alone",
        "industry": "Hollywood",
        "genre": ["Comedy", "Family"],
        "year": 1990,
        "description": "A young boy uses clever tricks to protect his home.",
        "poster": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQHK_FOnat28w5uhq1RKCyunssmIo-vrzuGpTukOIrigQ&s=10"
    },

    # CRIME
    {
        "title": "Raid 2",
        "industry": "Bollywood",
        "genre": ["Crime", "Thriller", "Drama"],
        "year": 2025,
        "description": "An income tax officer takes on a challenging investigation.",
        "poster": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRY_yGV4Li0ALyYyTDppdjUaFQxcCfi2scScy1hVV7_nA&s=10"
    },
    {
        "title": "Drishyam",
        "industry": "Bollywood",
        "genre": ["Crime", "Thriller", "Drama"],
        "year": 2015,
        "description": "A father tries to protect his family through a carefully planned strategy.",
        "poster": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4bIrAbs-gY6aco_k3MptkkbFOh3t7fcBbIa_6jeHL-A&s=10"
    },
    {
        "title": "Andhadhun",
        "industry": "Bollywood",
        "genre": ["Crime", "Thriller", "Comedy"],
        "year": 2018,
        "description": "A pianist becomes involved in a mysterious crime investigation.",
        "poster": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQZKbblxphnxBwo3c5zb4Rya87oBcLqPNJM1diG5HRqIw&s=10"
    },
    {
        "title": "Knives Out",
        "industry": "Hollywood",
        "genre": ["Crime", "Mystery", "Comedy"],
        "year": 2019,
        "description": "A detective investigates a mysterious death in a wealthy family.",
        "poster": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJ2jp2k4hSvAyRCprVfBeAAzh1P1_QqH_pl6thQveugA&s=10"
    },
    {
        "title": "The Batman",
        "industry": "Hollywood",
        "genre": ["Crime", "Action", "Drama"],
        "year": 2022,
        "description": "Batman investigates corruption and crime in Gotham City.",
        "poster": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSV9s1naV3T_h378vBhMYysfmMInSKzrbTXjFY49cJ2jQ&s=10"
    },

    # DRAMA
    {
        "title": "Saiyaara",
        "industry": "Bollywood",
        "genre": ["Romance", "Drama"],
        "year": 2025,
        "description": "A heartfelt musical love story about two aspiring artists.",
        "poster": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ2ctfgnuMUlVFX4gXQsV2aMMRu9GUcM1XvWP2wKJtVTA&s=10"
    },
    {
        "title": "12th Fail",
        "industry": "Bollywood",
        "genre": ["Drama"],
        "year": 2023,
        "description": "An inspiring story of determination and the pursuit of education.",
        "poster": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRkk7zJiCRM7mrzfL7wivMJ3pASGgl5OXnW2rNkKt43-A&s=10"
    },
    {
        "title": "Taare Zameen Par",
        "industry": "Bollywood",
        "genre": ["Drama"],
        "year": 2007,
        "description": "A teacher helps a young student discover his unique talents.",
        "poster": "https://image.tmdb.org/t/p/w500/66A9MqXOyVFCibj5w7k68UPEaJP.jpg"
    },
    {
        "title": "The Pursuit of Happyness",
        "industry": "Hollywood",
        "genre": ["Drama"],
        "year": 2006,
        "description": "A father works hard to build a better future for his son.",
        "poster": "https://image.tmdb.org/t/p/w500/rruAZO7zxqzzlSzgBv672BqW3cW.jpg"
    },
    {
        "title": "Oppenheimer",
        "industry": "Hollywood",
        "genre": ["Drama", "Thriller"],
        "year": 2023,
        "description": "A historical drama about the scientist behind the atomic bomb.",
        "poster": "https://image.tmdb.org/t/p/w500/8Gxv8gSFCU0LGDykEGv7vR1n2Wk.jpg"
    },

    # ROMANCE
    {
        "title": "Jab We Met",
        "industry": "Bollywood",
        "genre": ["Romance", "Comedy"],
        "year": 2007,
        "description": "Two strangers meet during a train journey and change each other's lives.",
        "poster": "https://image.tmdb.org/t/p/w500/mYKkjwwlxXnFf7Wn8G76Bq0M4yC.jpg"
    },
    {
        "title": "Yeh Jawaani Hai Deewani",
        "industry": "Bollywood",
        "genre": ["Romance", "Drama"],
        "year": 2013,
        "description": "Friends reunite and discover how their dreams and relationships have changed.",
        "poster": "https://image.tmdb.org/t/p/w500/v9Qz75t0G8X1B8M3v0N5Xv8m6z4.jpg"
    },
    {
        "title": "The Notebook",
        "industry": "Hollywood",
        "genre": ["Romance", "Drama"],
        "year": 2004,
        "description": "A romantic story following a couple through different stages of life.",
        "poster": "https://image.tmdb.org/t/p/w500/rqqMfm0C3Wgn6kvIVCVOTuNbWqX.jpg"
    },
    {
        "title": "La La Land",
        "industry": "Hollywood",
        "genre": ["Romance", "Drama", "Musical"],
        "year": 2016,
        "description": "A musician and an aspiring actor pursue their dreams in Los Angeles.",
        "poster": "https://image.tmdb.org/t/p/w500/uDO8zWDjaWwofdGCOhy5k5LUKWw.jpg"
    },

    # SCI-FI
    {
        "title": "Interstellar",
        "industry": "Hollywood",
        "genre": ["Sci-Fi", "Drama", "Adventure"],
        "year": 2014,
        "description": "Explorers travel through space in search of a future for humanity.",
        "poster": "https://image.tmdb.org/t/p/w500/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg"
    },
    {
        "title": "Inception",
        "industry": "Hollywood",
        "genre": ["Sci-Fi", "Action", "Thriller"],
        "year": 2010,
        "description": "A team enters dreams to carry out a complex mission.",
        "poster": "https://image.tmdb.org/t/p/w500/edv5CZvWj09upOsy2Y6IwDhK8bt.jpg"
    },
    {
        "title": "The Matrix",
        "industry": "Hollywood",
        "genre": ["Sci-Fi", "Action"],
        "year": 1999,
        "description": "A computer hacker discovers the surprising truth about reality.",
        "poster": "https://image.tmdb.org/t/p/w500/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg"
    },
    {
        "title": "Kalki 2898 AD",
        "industry": "Bollywood",
        "genre": ["Sci-Fi", "Action", "Adventure"],
        "year": 2024,
        "description": "A futuristic story inspired by Indian mythology.",
        "poster": "https://image.tmdb.org/t/p/w500/ombsmhYUqR4qqOLOxAyr5V8hbyv.jpg"
    },
    {
        "title": "Avatar",
        "industry": "Hollywood",
        "genre": ["Sci-Fi", "Adventure", "Action"],
        "year": 2009,
        "description": "A human joins the Na'vi on the extraordinary world of Pandora.",
        "poster": "https://image.tmdb.org/t/p/w500/kyeOwBBuCSRWLUK4y63Gj33yvj7.jpg"
    },

    # SPORTS
    {
        "title": "Chak De! India",
        "industry": "Bollywood",
        "genre": ["Sports", "Drama"],
        "year": 2007,
        "description": "A hockey coach leads a women's team towards a championship.",
        "poster": "https://image.tmdb.org/t/p/w500/66A9MqXOyVFCibj5w7k68UPEaJP.jpg"
    },
    {
        "title": "Dangal",
        "industry": "Bollywood",
        "genre": ["Sports", "Drama"],
        "year": 2016,
        "description": "A father trains his daughters to become successful wrestlers.",
        "poster": "https://image.tmdb.org/t/p/w500/jIux7vEgnoIaXm19uqqqE9g1Nl.jpg"
    },
    {
        "title": "Bhaag Milkha Bhaag",
        "industry": "Bollywood",
        "genre": ["Sports", "Drama"],
        "year": 2013,
        "description": "The inspiring life story of Indian athlete Milkha Singh.",
        "poster": "https://image.tmdb.org/t/p/w500/w1v48L5Xw48b8R8l88WjeWhT7S6.jpg"
    },
    {
        "title": "Ford v Ferrari",
        "industry": "Hollywood",
        "genre": ["Sports", "Drama"],
        "year": 2019,
        "description": "Engineers and drivers work together to challenge Ferrari at Le Mans.",
        "poster": "https://image.tmdb.org/t/p/w500/dLvU2AWK03SFGecMn7j1d5jHw58.jpg"
    },

    # THRILLER
    {
        "title": "Drishyam 2",
        "industry": "Bollywood",
        "genre": ["Thriller", "Crime", "Drama"],
        "year": 2022,
        "description": "A family faces new challenges as an old case returns.",
        "poster": "https://image.tmdb.org/t/p/w500/jIux7vEgnoIaXm19uqqqE9g1Nl.jpg"
    },
    {
        "title": "Talaash",
        "industry": "Bollywood",
        "genre": ["Thriller", "Crime", "Mystery"],
        "year": 2012,
        "description": "A police officer investigates a mysterious case.",
        "poster": "https://image.tmdb.org/t/p/w500/mYKkjwwlxXnFf7Wn8G76Bq0M4yC.jpg"
    },
    {
        "title": "Kahaani",
        "industry": "Bollywood",
        "genre": ["Thriller", "Mystery", "Drama"],
        "year": 2012,
        "description": "A woman searches for her missing husband in Kolkata.",
        "poster": "https://image.tmdb.org/t/p/w500/ombsmhYUqR4qqOLOxAyr5V8hbyv.jpg"
    },
    {
        "title": "Shutter Island",
        "industry": "Hollywood",
        "genre": ["Thriller", "Mystery", "Drama"],
        "year": 2010,
        "description": "Two investigators visit a remote island to investigate a disappearance.",
        "poster": "https://image.tmdb.org/t/p/w500/4GDy0FiInTwkKexurgoVqBPHC1t.jpg"
    },
    {
        "title": "Gone Girl",
        "industry": "Hollywood",
        "genre": ["Thriller", "Mystery", "Drama"],
        "year": 2014,
        "description": "A disappearance leads to a complicated investigation.",
        "poster": "https://image.tmdb.org/t/p/w500/qymaqaHMruFYkLwmhWPYn1P2j3Y.jpg"
    }
]

genre_counts = {}
for movie in movies:
    for genre in movie["genre"]:
        genre_counts[genre] = genre_counts.get(genre, 0) + 1

available_genres = sorted([
    genre for genre, count in genre_counts.items()
    if count >= 3
])

@app.route("/")
def home():
    return render_template("index.html", available_genres=available_genres)

@app.route("/recommend", methods=["POST"])
def recommend():
    industry = request.form.get("industry", "All")
    genre = request.form.get("genre", "All")

    filtered_movies = []
    for movie in movies:
        industry_match = (industry == "All" or movie["industry"] == industry)
        genre_match = (genre == "All" or genre in movie["genre"])
        if industry_match and genre_match:
            filtered_movies.append(movie)

    recommended_movies = filtered_movies[:5]

    return render_template(
        "recommendations.html",
        movies=recommended_movies,
        selected_industry=industry,
        selected_genre=genre
    )

@app.route("/watchlist")
def watchlist_page():
    return render_template("watchlist.html", movies=movies)

if __name__ == "__main__":
    app.run(debug=True)
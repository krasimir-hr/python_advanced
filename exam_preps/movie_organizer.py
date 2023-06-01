def movie_organizer(*movies_by_genre):
    genres = {}
    for movie, genre in movies_by_genre:
        if genre not in genres:
            genres[genre] = []
        genres[genre].append(movie)

    sorted_movies = sorted(genres.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ""
    for genre, movies in sorted_movies:
        movies = sorted(movies)
        result += f"{genre} - {len(movies)}\n"
        for movie in movies:
            result += f"* {movie}\n"

    return result.strip()

print(movie_organizer(

("The Godfather", "Drama"),

("The Hangover", "Comedy"),

("The Shawshank Redemption",

"Drama"),

("The Pursuit of Happiness",

"Drama"),

("The Hangover Part II", "Comedy")))
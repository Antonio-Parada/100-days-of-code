class MovieRecommender:
    def __init__(self):
        self.movies_by_genre = {
            "action": ["Die Hard", "The Dark Knight", "Mad Max: Fury Road"],
            "comedy": ["Anchorman", "Superbad", "The Hangover"],
            "drama": ["The Shawshank Redemption", "Forrest Gump", "Pulp Fiction"],
            "sci-fi": ["Blade Runner 2049", "Interstellar", "Arrival"]
        }

    def recommend_by_genre(self, preferred_genre):
        preferred_genre_lower = preferred_genre.lower()
        if preferred_genre_lower in self.movies_by_genre:
            movies = self.movies_by_genre[preferred_genre_lower]
            return f"If you like {preferred_genre}, you might enjoy: {', '.join(movies)}."
        else:
            return "Sorry, I don't have recommendations for that genre. Try action, comedy, drama, or sci-fi."

if __name__ == "__main__":
    recommender = MovieRecommender()
    print("--- Simple CLI Movie Recommender (Rule-based) ---")
    print("Tell me your preferred movie genre (e.g., action, comedy, drama, sci-fi).")
    print("Type 'exit' to quit.")

    while True:
        user_input = input("Your preferred genre: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        recommendation = recommender.recommend_by_genre(user_input)
        print(f"Recommender: {recommendation}")

class MusicSuggestor:
    def __init__(self):
        self.music_genres = {
            "rock": ["Led Zeppelin", "Queen", "AC/DC"],
            "pop": ["Taylor Swift", "Ed Sheeran", "Adele"],
            "classical": ["Beethoven", "Mozart", "Bach"],
            "jazz": ["Louis Armstrong", "Miles Davis", "John Coltrane"]
        }

    def suggest_music_by_genre(self, preferred_genre):
        preferred_genre_lower = preferred_genre.lower()
        if preferred_genre_lower in self.music_genres:
            artists = self.music_genres[preferred_genre_lower]
            return f"If you like {preferred_genre}, you might enjoy artists like: {', '.join(artists)}."
        else:
            return "Sorry, I don't have suggestions for that genre. Try rock, pop, classical, or jazz."

if __name__ == "__main__":
    suggestor = MusicSuggestor()
    print("--- Simple CLI Music Suggestor (Rule-based) ---")
    print("Tell me your preferred music genre (e.g., rock, pop, classical, jazz).")
    print("Type 'exit' to quit.")

    while True:
        user_input = input("Your preferred genre: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        suggestion = suggestor.suggest_music_by_genre(user_input)
        print(f"Suggestor: {suggestion}")
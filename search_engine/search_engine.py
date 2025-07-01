class SimpleSearchEngine:
    def __init__(self):
        self.documents = {}
        self.index = {}
        self.doc_id_counter = 0

    def add_document(self, document_text):
        doc_id = self.doc_id_counter
        self.documents[doc_id] = document_text
        words = document_text.lower().split()
        for word in words:
            if word not in self.index:
                self.index[word] = set()
            self.index[word].add(doc_id)
        self.doc_id_counter += 1
        return doc_id

    def search(self, query):
        query_words = query.lower().split()
        if not query_words:
            return []

        results = set()
        first_word = True

        for word in query_words:
            if word in self.index:
                if first_word:
                    results = self.index[word]
                    first_word = False
                else:
                    results = results.intersection(self.index[word])
            else:
                return [] # If any word is not found, no results
        
        # Return the original documents for the matching doc_ids
        return [self.documents[doc_id] for doc_id in results]

if __name__ == "__main__":
    engine = SimpleSearchEngine()
    engine.add_document("The quick brown fox jumps over the lazy dog.")
    engine.add_document("Never jump over a lazy dog.")
    engine.add_document("The quick brown cat is fast.")

    print("Searching for 'lazy dog':")
    for result in engine.search("lazy dog"):
        print(f"- {result}")

    print("\nSearching for 'quick brown':")
    for result in engine.search("quick brown"):
        print(f"- {result}")

    print("\nSearching for 'cat':")
    for result in engine.search("cat"):
        print(f"- {result}")

    print("\nSearching for 'nonexistent':")
    for result in engine.search("nonexistent"):
        print(f"- {result}")

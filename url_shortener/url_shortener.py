import hashlib
import base64

class URLShortener:
    def __init__(self):
        self.url_map = {}
        self.base_url = "http://short.url/"

    def shorten_url(self, long_url):
        # Generate a simple hash of the URL
        hash_object = hashlib.md5(long_url.encode())
        hex_dig = hash_object.hexdigest()
        
        # Take a portion of the hash and encode it in base64 for a shorter string
        short_code = base64.urlsafe_b64encode(hex_dig[:6].encode()).decode().rstrip('=')

        # Store the mapping
        self.url_map[short_code] = long_url
        return self.base_url + short_code

    def retrieve_long_url(self, short_url):
        short_code = short_url.replace(self.base_url, '')
        return self.url_map.get(short_code, "Short URL not found.")

if __name__ == "__main__":
    shortener = URLShortener()
    print("--- Simple CLI URL Shortener ---")
    print("Commands: shorten <URL>, retrieve <SHORT_URL>, exit")

    while True:
        command_input = input("> ").split(maxsplit=1)
        cmd = command_input[0].lower()

        if cmd == "shorten":
            if len(command_input) == 2:
                long_url = command_input[1]
                short_url = shortener.shorten_url(long_url)
                print(f"Shortened URL: {short_url}")
            else:
                print("Usage: shorten <URL>")
        elif cmd == "retrieve":
            if len(command_input) == 2:
                short_url = command_input[1]
                long_url = shortener.retrieve_long_url(short_url)
                print(f"Original URL: {long_url}")
            else:
                print("Usage: retrieve <SHORT_URL>")
        elif cmd == "exit":
            print("Exiting URL Shortener.")
            break
        else:
            print("Unknown command.")

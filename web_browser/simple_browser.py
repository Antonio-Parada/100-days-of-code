import webbrowser
import sys

def open_url_in_browser(url):
    try:
        webbrowser.open(url)
        print(f"Opened '{url}' in your default web browser.")
    except webbrowser.Error as e:
        print(f"Error opening browser: {e}")

if __name__ == "__main__":
    print("--- Simple Web Browser (using default system browser) ---")
    if len(sys.argv) > 1:
        url_to_open = sys.argv[1]
        if not url_to_open.startswith(("http://", "https://")):
            url_to_open = "http://" + url_to_open
        open_url_in_browser(url_to_open)
    else:
        print("Usage: python simple_browser.py <URL>")
        print("Example: python simple_browser.py google.com")

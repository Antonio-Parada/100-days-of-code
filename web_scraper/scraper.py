import requests
from bs4 import BeautifulSoup
import random
import time

# List of user-agents to rotate through
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0',
]

# List of proxies to rotate through (replace with your own proxies)
# Example format: 'http://user:pass@host:port'
PROXIES = [
    # Add your proxies here
]

def scrape_title(url, use_proxies=False, delay=1):
    """
    Fetches the HTML content of a URL using a random user-agent and optional proxy,
    and returns its title. Includes a delay between requests.
    """
    try:
        # Introduce a delay to be a responsible scraper
        time.sleep(delay)

        # Choose a random user-agent
        user_agent = random.choice(USER_AGENTS)
        headers = {'User-Agent': user_agent}

        proxies = None
        if use_proxies and PROXIES:
            proxy = random.choice(PROXIES)
            proxies = {
                'http': proxy,
                'https': proxy,
            }

        print(f"Scraping {url}...")
        response = requests.get(url, headers=headers, proxies=proxies, timeout=10)
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.title.string.strip() if soup.title else "No title found"

    except requests.exceptions.RequestException as e:
        return f"Error fetching URL: {e}"

if __name__ == "__main__":
    # Example usage with rate limiting:
    target_urls = [
        "http://example.com",
        "http://example.com", # Scraping the same page again to show delay
        "http://example.com",
    ]
    
    print("--- Scraping with a 2-second delay between requests ---")
    for url in target_urls:
        title = scrape_title(url, delay=2)
        print(f"Page Title: {title}\n")

    # To scrape with proxies (make sure to add proxies to the PROXIES list):
    if PROXIES:
        print("\n--- Scraping with proxies and a 3-second delay ---")
        for url in target_urls:
            title_with_proxy = scrape_title(url, use_proxies=True, delay=3)
            print(f"Page Title (with proxy): {title_with_proxy}\n")
    else:
        print("\nNo proxies configured. Skipping proxy test.")

import requests
from bs4 import BeautifulSoup
import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

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

        print(f"Scraping {url} with requests...")
        response = requests.get(url, headers=headers, proxies=proxies, timeout=10)
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.title.string.strip() if soup.title else "No title found"

    except requests.exceptions.RequestException as e:
        return f"Error fetching URL: {e}"

def scrape_with_selenium(url, delay=2):
    """
    Fetches the HTML content of a URL using Selenium to handle dynamic content,
    and returns its title.
    """
    try:
        # Set up headless Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument(f"user-agent={random.choice(USER_AGENTS)}")

        # Set up the Chrome driver
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

        print(f"Scraping {url} with Selenium...")
        driver.get(url)

        # Wait for the page to load (adjust as needed)
        time.sleep(delay)

        title = driver.title
        driver.quit()
        return title

    except Exception as e:
        return f"Error scraping with Selenium: {e}"

if __name__ == "__main__":
    # Example usage of the original scraper:
    target_url = "http://example.com"
    print("--- Scraping with requests ---")
    title = scrape_title(target_url)
    print(f"Page Title: {title}\n")

    # Example usage of the Selenium scraper:
    # This is useful for pages that load content with JavaScript.
    print("--- Scraping with Selenium ---")
    dynamic_title = scrape_with_selenium(target_url)
    print(f"Page Title (dynamic): {dynamic_title}\n")

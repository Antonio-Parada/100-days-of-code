import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # For demonstration, let's extract all paragraph texts
        paragraphs = soup.find_all('p')
        for p in paragraphs:
            print(p.get_text())
            
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    target_url = input("Enter the URL to scrape: ")
    scrape_website(target_url)

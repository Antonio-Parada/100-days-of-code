import requests
import sys

# You need to get an API key from NewsAPI.org
# Sign up at: https://newsapi.org/
API_KEY = "YOUR_NEWSAPI_KEY"
BASE_URL = "https://newsapi.org/v2/top-headlines"

def get_top_headlines(country='us', category=None):
    if API_KEY == "YOUR_NEWSAPI_KEY":
        print("Please replace 'YOUR_NEWSAPI_KEY' with your actual NewsAPI.org API key.")
        return

    params = {
        'apiKey': API_KEY,
        'country': country
    }
    if category:
        params['category'] = category

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data['status'] == 'ok':
            articles = data['articles']
            if not articles:
                print("No articles found.")
                return

            print(f"\n--- Top Headlines ({country.upper()}{f' - {category.capitalize()}' if category else ''}) ---")
            for i, article in enumerate(articles):
                print(f"{i+1}. {article['title']}")
                print(f"   Source: {article['source']['name']}")
                print(f"   URL: {article['url']}")
                print("--------------------------------------------------")
        else:
            print(f"Error: {data['message']}")

    except requests.exceptions.RequestException as e:
        print(f"Error connecting to news service: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    print("--- Simple News Aggregator ---")
    print("Usage: python news_aggregator.py [country_code] [category]")
    print("Example: python news_aggregator.py us technology")
    print("Default: Top headlines from US.")

    country_code = 'us'
    category = None

    if len(sys.argv) > 1:
        country_code = sys.argv[1].lower()
    if len(sys.argv) > 2:
        category = sys.argv[2].lower()

    get_top_headlines(country_code, category)

import requests
from bs4 import BeautifulSoup
import csv
import json
from urllib.parse import urljoin
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
import time
import random
import logging

# Configure logging to file
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='scraper.log', filemode='a')

# Sample User-Agents (you can expand this list)
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/110.0.1587.63',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/110.0',
]

def get_random_user_agent():
    return random.choice(USER_AGENTS)

def solve_captcha_placeholder():
    logging.info("Attempting to solve CAPTCHA (placeholder for external service/manual intervention).")
    # In a real scenario, this would integrate with a CAPTCHA solving service
    # or provide a mechanism for manual input.
    return True # Assume success for now

def save_to_csv(data, filename):

# Sample User-Agents (you can expand this list)
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/110.0.1587.63',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/110.0',
]

def get_random_user_agent():
    return random.choice(USER_AGENTS)

def save_to_csv(data, filename):
    if not data:
        print("No data to save.")
        return
    
    keys = data[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)
    print(f"Data saved to {filename}")

def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as output_file:
        json.dump(data, output_file, indent=4)
    print(f"Data saved to {filename}")

def scrape_static_website(url, extract_type='text', tag=None, class_name=None, proxies=None):
    extracted_data = []
    headers = {'User-Agent': get_random_user_agent()}
    try:
        print(f"Attempting to scrape (static): {url}")
        response = requests.get(url, timeout=10, headers=headers, proxies=proxies) # Add timeout, headers, proxies
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        if extract_type == 'text':
            elements = soup.find_all(tag, class_=class_name) if tag else soup.find_all('p')
            for elem in elements:
                extracted_data.append({'text': elem.get_text(strip=True)})
        elif extract_type == 'links':
            for link in soup.find_all('a', href=True):
                extracted_data.append({'text': link.get_text(strip=True), 'href': link['href']})
        elif extract_type == 'images':
            for img in soup.find_all('img', src=True):
                extracted_data.append({'alt': img.get('alt', ''), 'src': img['src']})
        else:
            print("Invalid extraction type. Supported types: text, links, images.")
            return []

    except requests.exceptions.Timeout:
        print(f"Error: Request timed out for {url}")
    except requests.exceptions.HTTPError as e:
        print(f"Error: HTTP error occurred for {url} - {e.response.status_code} {e.response.reason}")
    except requests.exceptions.ConnectionError as e:
        print(f"Error: Could not connect to {url} - {e}")
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
    except Exception as e:
        print(f"An unexpected error occurred during static scraping: {e}")
    
    return extracted_data

def scrape_dynamic_website(url, extract_type='text', tag=None, class_name=None, wait_for_element=None, proxies=None):
    extracted_data = []
    driver = None
    try:
        # Setup Chrome options for headless browsing and user agent
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument(f'user-agent={get_random_user_agent()}')
        if proxies:
            proxy = random.choice(list(proxies.values()))
            options.add_argument(f'--proxy-server={proxy}')

        # You might need to specify the path to your chromedriver executable
        # service = Service('/path/to/chromedriver')
        # driver = webdriver.Chrome(service=service, options=options)
        driver = webdriver.Chrome(options=options) # Assumes chromedriver is in PATH

        print(f"Attempting to scrape (dynamic): {url}")
        driver.get(url)

        if wait_for_element:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, wait_for_element))
            )
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        if extract_type == 'text':
            elements = soup.find_all(tag, class_=class_name) if tag else soup.find_all('p')
            for elem in elements:
                extracted_data.append({'text': elem.get_text(strip=True)})
        elif extract_type == 'links':
            for link in soup.find_all('a', href=True):
                extracted_data.append({'text': link.get_text(strip=True), 'href': link['href']})
        elif extract_type == 'images':
            for img in soup.find_all('img', src=True):
                extracted_data.append({'alt': img.get('alt', ''), 'src': img['src']})
        else:
            print("Invalid extraction type. Supported types: text, links, images.")
            return []

    except TimeoutException:
        print(f"Error: Timed out waiting for element {wait_for_element} on {url}")
    except WebDriverException as e:
        print(f"WebDriver error: {e}. Make sure chromedriver is installed and in your PATH.")
    except Exception as e:
        print(f"An unexpected error occurred during dynamic scraping: {e}")
    finally:
        if driver:
            driver.quit()
    
    return extracted_data

def scrape_website(url, extract_type='text', tag=None, class_name=None, output_file=None, output_format='csv', max_pages=1, current_page=1, dynamic_scrape=False, wait_for_element=None, proxies=None, delay=0):
    all_extracted_data = []
    
    if dynamic_scrape:
        extracted_data_current_page = scrape_dynamic_website(url, extract_type, tag, class_name, wait_for_element, proxies)
    else:
        extracted_data_current_page = scrape_static_website(url, extract_type, tag, class_name, proxies)

    all_extracted_data.extend(extracted_data_current_page)

    # Handle pagination (only for static scraping for simplicity with current dynamic setup)
    if not dynamic_scrape and current_page < max_pages:
        time.sleep(delay) # Add delay for politeness
        try:
            response = requests.get(url, timeout=10, headers={'User-Agent': get_random_user_agent()}, proxies=proxies)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            next_page_link = soup.find('a', text=re.compile(r'next', re.IGNORECASE))
            if next_page_link and next_page_link.get('href'):
                next_page_url = urljoin(url, next_page_link['href'])
                all_extracted_data.extend(scrape_website(next_page_url, extract_type, tag, class_name, None, output_format, max_pages, current_page + 1, dynamic_scrape, wait_for_element, proxies, delay))
        except requests.exceptions.RequestException as e:
            print(f"Error during pagination check: {e}")

    if output_file and current_page == 1: # Only save to file once, after all pages are scraped
        if output_format == 'csv':
            save_to_csv(all_extracted_data, output_file)
        elif output_format == 'json':
            save_to_json(all_extracted_data, output_file)
        else:
            print("Invalid output format. Supported formats: csv, json.")
    elif not output_file:
        for item in extracted_data_current_page:
            print(item)
        
    return all_extracted_data

if __name__ == "__main__":
    target_url = input("Enter the URL to scrape: ")
    extract_choice = input("What do you want to extract? (text, links, images): ").lower()
    tag_name = input("Enter HTML tag to extract (e.g., p, h1, div) or leave blank for default: ")
    class_name = input("Enter CSS class name (optional): ")
    output_filename = input("Enter output filename (e.g., output.csv, output.json) or leave blank to print to console: ")
    output_file_format = ''
    if output_filename:
        output_file_format = input("Enter output format (csv, json): ").lower()
    
    max_pages_input = input("Enter maximum number of pages to scrape (default: 1): ")
    max_pages = int(max_pages_input) if max_pages_input.isdigit() else 1

    dynamic_scrape_choice = input("Use dynamic scraping (for JavaScript-rendered pages)? (yes/no): ").lower()
    dynamic_scrape = dynamic_scrape_choice == 'yes'

    wait_for_element_css = None
    if dynamic_scrape:
        wait_for_element_css = input("Enter CSS selector for an element to wait for (optional, e.g., #content): ")
        if not wait_for_element_css:
            wait_for_element_css = None

    proxy_input = input("Enter proxy (e.g., http://user:pass@host:port or leave blank): ")
    proxies = {"http": proxy_input, "https": proxy_input} if proxy_input else None

    delay_input = input("Enter delay between requests in seconds (default: 0): ")
    delay = float(delay_input) if delay_input.replace('.', '').isdigit() else 0

    scrape_website(target_url, extract_choice, tag_name if tag_name else None, class_name if class_name else None, output_filename if output_filename else None, output_file_format, max_pages, dynamic_scrape=dynamic_scrape, wait_for_element=wait_for_element_css, proxies=proxies, delay=delay)

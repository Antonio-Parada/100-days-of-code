import requests
from bs4 import BeautifulSoup
import csv
import json
from urllib.parse import urljoin

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

def scrape_website(url, extract_type='text', tag=None, class_name=None, output_file=None, output_format='csv', max_pages=1, current_page=1):
    all_extracted_data = []
    try:
        print(f"Attempting to scrape: {url} (Page {current_page})")
        response = requests.get(url, timeout=10) # Add timeout
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        extracted_data_current_page = []
        if extract_type == 'text':
            elements = soup.find_all(tag, class_=class_name) if tag else soup.find_all('p')
            for elem in elements:
                extracted_data_current_page.append({'text': elem.get_text(strip=True)})
        elif extract_type == 'links':
            for link in soup.find_all('a', href=True):
                extracted_data_current_page.append({'text': link.get_text(strip=True), 'href': link['href']})
        elif extract_type == 'images':
            for img in soup.find_all('img', src=True):
                extracted_data_current_page.append({'alt': img.get('alt', ''), 'src': img['src']})
        else:
            print("Invalid extraction type. Supported types: text, links, images.")
            return

        all_extracted_data.extend(extracted_data_current_page)

        # Handle pagination
        if current_page < max_pages:
            next_page_link = soup.find('a', text=re.compile(r'next', re.IGNORECASE))
            if next_page_link and next_page_link.get('href'):
                next_page_url = urljoin(url, next_page_link['href'])
                all_extracted_data.extend(scrape_website(next_page_url, extract_type, tag, class_name, None, output_format, max_pages, current_page + 1))

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
            
    except requests.exceptions.Timeout:
        print(f"Error: Request timed out for {url}")
    except requests.exceptions.HTTPError as e:
        print(f"Error: HTTP error occurred for {url} - {e.response.status_code} {e.response.reason}")
    except requests.exceptions.ConnectionError as e:
        print(f"Error: Could not connect to {url} - {e}")
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
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

    scrape_website(target_url, extract_choice, tag_name if tag_name else None, class_name if class_name else None, output_filename if output_filename else None, output_file_format, max_pages)

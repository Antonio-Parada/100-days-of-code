from bs4 import BeautifulSoup

class DealFinder:
    def __init__(self):
        self.tracked_products = []

    def add_product_to_track(self, product_name, target_price, url):
        self.tracked_products.append({
            'name': product_name,
            'target_price': target_price,
            'url': url,
            'last_known_price': None
        })
        print(f"Tracking '{product_name}' with target price {target_price} from {url}")

    def _get_dummy_html_content(self, product_name, current_price):
        # Simulate fetching HTML content from a product page
        return f"""
        <html>
        <head><title>{product_name} - Product Page</title></head>
        <body>
            <h1>{product_name}</h1>
            <p class="price">${current_price}</p>
            <div id="product-details">
                <span>Some other details</span>
                <span class="old-price">$100.00</span>
            </div>
        </body>
        </html>
        """

    def check_for_deals(self):
        print("\n--- Checking for Deals ---")
        for product in self.tracked_products:
            # In a real app, you'd fetch content from product['url']
            # For this simulation, we'll use a dummy content with a changing price
            import random
            simulated_price = round(product['target_price'] + random.uniform(-10, 10), 2)
            if simulated_price < 0: simulated_price = 5.00 # Ensure price is not negative

            html_content = self._get_dummy_html_content(product['name'], simulated_price)
            soup = BeautifulSoup(html_content, 'html.parser')
            
            price_tag = soup.find('p', class_='price')
            if price_tag:
                current_price_str = price_tag.text.replace('$', '')
                try:
                    current_price = float(current_price_str)
                    product['last_known_price'] = current_price

                    if current_price <= product['target_price']:
                        print(f"DEAL ALERT! '{product['name']}' is now ${current_price} (Target: ${product['target_price']}) at {product['url']}")
                    else:
                        print(f"'{product['name']}' is ${current_price} (Target: ${product['target_price']}) - No deal yet.")
                except ValueError:
                    print(f"Could not parse price for '{product['name']}'.")
            else:
                print(f"Could not find price for '{product['name']}'.")
        print("--------------------------")

if __name__ == "__main__":
    finder = DealFinder()
    print("--- Simple CLI Deal Finder Simulation (requires BeautifulSoup: pip install beautifulsoup4) ---")
    print("Commands: add <product_name> <target_price> <url>, check, exit")

    while True:
        command_input = input("> ").split(maxsplit=3)
        cmd = command_input[0].lower()

        if cmd == "add":
            if len(command_input) == 4:
                try:
                    product_name = command_input[1]
                    target_price = float(command_input[2])
                    url = command_input[3]
                    finder.add_product_to_track(product_name, target_price, url)
                except ValueError:
                    print("Target price must be a number.")
            else:
                print("Usage: add <product_name> <target_price> <url>")
        elif cmd == "check":
            finder.check_for_deals()
        elif cmd == "exit":
            print("Exiting Deal Finder.")
            break
        else:
            print("Unknown command.")

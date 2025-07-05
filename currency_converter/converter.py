import requests

class CurrencyConverter:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://open.er-api.com/v6/latest/"

    def get_exchange_rate(self, base_currency, target_currency):
        url = f"{self.base_url}{base_currency}"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200 and data["result"] == "success":
            rates = data["rates"]
            if target_currency in rates:
                return rates[target_currency]
            else:
                print(f"Error: Target currency {target_currency} not found.")
                return None
        else:
            print(f"Error fetching exchange rates: {data.get("error-type", "Unknown error")}")
            return None

    def convert(self, amount, base_currency, target_currency):
        rate = self.get_exchange_rate(base_currency, target_currency)
        if rate:
            return amount * rate
        return None

if __name__ == "__main__":
    # Replace with your actual API key from https://open.er-api.com/
    # For demonstration purposes, a placeholder is used.
    API_KEY = "YOUR_API_KEY"
    converter = CurrencyConverter(API_KEY)

    amount_to_convert = 100
    from_currency = "USD"
    to_currency = "EUR"

    converted_amount = converter.convert(amount_to_convert, from_currency, to_currency)

    if converted_amount is not None:
        print(f"{amount_to_convert} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

    # Example with an invalid currency
    converted_amount_invalid = converter.convert(50, "USD", "XYZ")

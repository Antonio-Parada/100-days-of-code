class CurrencyConverter:
    def __init__(self):
        self.exchange_rates = {
            "USD": {"EUR": 0.85, "GBP": 0.75, "JPY": 110.0},
            "EUR": {"USD": 1.18, "GBP": 0.88, "JPY": 129.0},
            "GBP": {"USD": 1.33, "EUR": 1.14, "JPY": 147.0},
            "JPY": {"USD": 0.0091, "EUR": 0.0078, "GBP": 0.0068}
        }

    def convert(self, amount, from_currency, to_currency):
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency == to_currency:
            return amount

        if from_currency not in self.exchange_rates:
            return "Error: Invalid 'from' currency."

        if to_currency not in self.exchange_rates[from_currency]:
            return "Error: Invalid 'to' currency for the given 'from' currency."

        rate = self.exchange_rates[from_currency][to_currency]
        converted_amount = amount * rate
        return converted_amount

if __name__ == '__main__':
    converter = CurrencyConverter()
    print("--- Interactive Currency Converter ---")
    print("Available currencies: USD, EUR, GBP, JPY")
    
    while True:
        try:
            amount_str = input("Enter amount to convert (or 'q' to quit): ")
            if amount_str.lower() == 'q':
                break
            amount = float(amount_str)

            from_currency = input("Convert from (e.g., USD): ").upper()
            to_currency = input("Convert to (e.g., EUR): ").upper()

            result = converter.convert(amount, from_currency, to_currency)
            print(f"{amount} {from_currency} = {result} {to_currency}")

        except ValueError:
            print("Invalid amount. Please enter a number.")
        except EOFError:
            print("Exiting converter.")
            break

    print("Converter finished.")
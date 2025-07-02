class RomanDecimalConverter:
    def __init__(self):
        self.roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def roman_to_decimal(self, roman_numeral):
        decimal_value = 0
        i = 0
        while i < len(roman_numeral):
            # Look at the current and next character
            current_char = roman_numeral[i]
            current_value = self.roman_map.get(current_char, 0)

            if i + 1 < len(roman_numeral):
                next_char = roman_numeral[i+1]
                next_value = self.roman_map.get(next_char, 0)

                if current_value < next_value:
                    decimal_value += (next_value - current_value)
                    i += 2
                else:
                    decimal_value += current_value
                    i += 1
            else:
                decimal_value += current_value
                i += 1
        return decimal_value

    def decimal_to_roman(self, decimal_num):
        if not (0 < decimal_num < 4000):
            return "Error: Decimal number out of range (1-3999)."

        roman_numerals = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
            (1, 'I')
        ]

        roman_string = ""
        for value, numeral in roman_numerals:
            while decimal_num >= value:
                roman_string += numeral
                decimal_num -= value
        return roman_string

if __name__ == '__main__':
    converter = RomanDecimalConverter()
    print("--- Interactive Roman to Decimal Converter ---")
    
    while True:
        choice = input("Convert (R)oman to Decimal or (D)ecimal to Roman? (q to quit): ").lower()
        if choice == 'q':
            break

        if choice == 'r':
            roman_numeral = input("Enter Roman numeral: ").upper()
            result = converter.roman_to_decimal(roman_numeral)
            print(f"Decimal: {result}")
        elif choice == 'd':
            try:
                decimal_num = int(input("Enter decimal number (1-3999): "))
                result = converter.decimal_to_roman(decimal_num)
                print(f"Roman: {result}")
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            print("Invalid choice. Please enter 'R', 'D', or 'q'.")

    print("Converter finished.")

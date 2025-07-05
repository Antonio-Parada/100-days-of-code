def roman_to_int(s: str) -> int:
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0
    for char in reversed(s):
        value = roman_map[char]
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value
    return result

def int_to_roman(num: int) -> str:
    if not (0 < num < 4000):
        raise ValueError("Number out of range (1-3999)")

    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num

if __name__ == "__main__":
    # Test Roman to Integer
    print(f"III -> {roman_to_int('III')}")      # Expected: 3
    print(f"LVIII -> {roman_to_int('LVIII')}")    # Expected: 58
    print(f"MCMXCIV -> {roman_to_int('MCMXCIV')}") # Expected: 1994

    print("\n" + "-"*20 + "\n")

    # Test Integer to Roman
    print(f"3 -> {int_to_roman(3)}")        # Expected: III
    print(f"58 -> {int_to_roman(58)}")      # Expected: LVIII
    print(f"1994 -> {int_to_roman(1994)}")    # Expected: MCMXCIV

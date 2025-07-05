import re

def solve_day_1_part_1(lines):
    total_sum = 0
    for line in lines:
        digits = re.findall(r'\d', line)
        if digits:
            calibration_value = int(digits[0] + digits[-1])
            total_sum += calibration_value
    return total_sum

if __name__ == "__main__":
    test_lines = [
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet",
    ]
    result = solve_day_1_part_1(test_lines)
    print(f"Test result: {result}") # Expected: 142

    # To solve with actual input, read from a file:
    # with open('input.txt', 'r') as f:
    #     input_lines = f.readlines()
    # actual_result = solve_day_1_part_1(input_lines)
    # print(f"Actual result: {actual_result}")

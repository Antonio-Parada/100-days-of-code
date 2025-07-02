def solve_day_1_part_1(data):
    max_calories = 0
    current_calories = 0
    for line in data.splitlines():
        if line:
            current_calories += int(line)
        else:
            max_calories = max(max_calories, current_calories)
            current_calories = 0
    max_calories = max(max_calories, current_calories) # Check last elf
    return max_calories

if __name__ == '__main__':
    # Test Case 1: Example from Advent of Code Day 1
    test_data = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""
    expected_result = 24000
    result = solve_day_1_part_1(test_data)
    print(f"Test Case 1 Result: {result} (Expected: {expected_result})")
    assert result == expected_result, "Test Case 1 Failed"
    print("Test Case 1 Passed")

    # You would typically read your actual input data from a file here
    # with open('input_day1.txt', 'r') as f:
    #     input_data = f.read()
    # final_answer = solve_day_1_part_1(input_data)
    # print(f"Final Answer: {final_answer}")

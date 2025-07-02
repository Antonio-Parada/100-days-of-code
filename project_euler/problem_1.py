def solve_problem_1(limit):
    total_sum = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            total_sum += i
    return total_sum

if __name__ == '__main__':
    # Test case for numbers below 10
    test_limit = 10
    expected_sum = 23
    result = solve_problem_1(test_limit)
    print(f"Sum of multiples of 3 or 5 below {test_limit}: {result} (Expected: {expected_sum})")
    assert result == expected_sum, "Test Case Failed: Incorrect sum for limit 10"
    print("Test Case Passed")

    # Solve for numbers below 1000
    final_limit = 1000
    final_result = solve_problem_1(final_limit)
    print(f"\nSum of multiples of 3 or 5 below {final_limit}: {final_result}")

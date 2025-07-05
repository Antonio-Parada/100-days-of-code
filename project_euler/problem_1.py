def solve_problem_1(limit=1000):
    total_sum = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            total_sum += i
    return total_sum

if __name__ == "__main__":
    result = solve_problem_1()
    print(f"The sum of all multiples of 3 or 5 below 1000 is: {result}")
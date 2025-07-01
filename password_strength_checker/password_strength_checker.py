import re

def check_password_strength(password):
    score = 0
    comments = []

    # Criteria 1: Length
    if len(password) >= 8:
        score += 1
    else:
        comments.append("Password should be at least 8 characters long.")

    # Criteria 2: Uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        comments.append("Password should contain uppercase letters.")

    # Criteria 3: Lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        comments.append("Password should contain lowercase letters.")

    # Criteria 4: Numbers
    if re.search(r"\d", password):
        score += 1
    else:
        comments.append("Password should contain numbers.")

    # Criteria 5: Special characters
    if re.search(r"[^a-zA-Z0-9]", password):
        score += 1
    else:
        comments.append("Password should contain special characters.")

    if score == 5:
        strength = "Very Strong"
    elif score >= 3:
        strength = "Strong"
    elif score >= 1:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, comments

if __name__ == "__main__":
    print("--- Simple CLI Password Strength Checker ---")
    print("Type a password to check its strength (or 'exit' to quit).")

    while True:
        user_input = input("Enter password: ")
        if user_input.lower() == "exit":
            print("Exiting Password Strength Checker.")
            break
        
        strength, comments = check_password_strength(user_input)
        print(f"Password Strength: {strength}")
        if comments:
            print("Suggestions:")
            for comment in comments:
                print(f"- {comment}")

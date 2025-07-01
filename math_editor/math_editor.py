def convert_to_latex(expression):
    # Very basic conversion for demonstration purposes
    # This would be much more complex for a real math editor
    
    expression = expression.replace("plus", "+")
    expression = expression.replace("minus", "-")
    expression = expression.replace("times", "\\times")
    expression = expression.replace("divided by", "\\div")
    expression = expression.replace("power of", "^")
    expression = expression.replace("square root of", "\\sqrt{") + "}"
    expression = expression.replace("fraction", "\\frac{") + "}{" + "}"

    # Handle common functions
    expression = expression.replace("sin(", "\\sin(")
    expression = expression.replace("cos(", "\\cos(")
    expression = expression.replace("tan(", "\\tan(")
    expression = expression.replace("log(", "\\log(")

    return f"${expression}$"

if __name__ == "__main__":
    print("--- Simple Math Editor (Text to LaTeX Converter) ---")
    print("Type mathematical expressions using simple English words (e.g., 'x plus y', 'a power of 2').")
    print("Type 'exit' to quit.")

    while True:
        user_input = input("Enter expression: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        latex_output = convert_to_latex(user_input)
        print(f"LaTeX: {latex_output}")

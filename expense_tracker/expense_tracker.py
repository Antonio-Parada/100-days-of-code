from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, description=""):
        try:
            amount = float(amount)
            if amount <= 0:
                print("Amount must be positive.")
                return
            self.expenses.append({
                'amount': amount,
                'category': category.lower(),
                'description': description,
                'date': datetime.now()
            })
            print(f"Added {amount:.2f} to {category} for '{description}'.")
        except ValueError:
            print("Invalid amount. Please enter a number.")

    def get_summary_by_category(self):
        summary = {}
        for expense in self.expenses:
            summary[expense['category']] = summary.get(expense['category'], 0) + expense['amount']
        
        print("\n--- Expense Summary by Category ---")
        if not summary:
            print("No expenses recorded yet.")
            return
        for category, total_amount in summary.items():
            print(f"{category.capitalize()}: {total_amount:.2f}")
        print("----------------------------------")

    def get_total_expenses(self):
        total = sum(expense['amount'] for expense in self.expenses)
        print(f"\nTotal Expenses: {total:.2f}")
        return total

if __name__ == "__main__":
    tracker = ExpenseTracker()
    print("--- Simple CLI Expense Tracker ---")
    print("Commands: add <amount> <category> [description], summary, total, exit")

    while True:
        command_input = input("> ").split(maxsplit=3)
        cmd = command_input[0].lower()

        if cmd == "add":
            if len(command_input) >= 3:
                amount = command_input[1]
                category = command_input[2]
                description = command_input[3] if len(command_input) == 4 else ""
                tracker.add_expense(amount, category, description)
            else:
                print("Usage: add <amount> <category> [description]")
        elif cmd == "summary":
            tracker.get_summary_by_category()
        elif cmd == "total":
            tracker.get_total_expenses()
        elif cmd == "exit":
            print("Exiting Expense Tracker.")
            break
        else:
            print("Unknown command.")

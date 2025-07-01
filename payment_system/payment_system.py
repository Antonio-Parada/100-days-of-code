class PaymentSystem:
    def __init__(self):
        self.accounts = {}
        self.transaction_id_counter = 0

    def create_account(self, username, initial_balance=0):
        if username in self.accounts:
            print(f"Account for {username} already exists.")
            return False
        self.accounts[username] = {'balance': initial_balance, 'transactions': []}
        print(f"Account for {username} created with initial balance {initial_balance}.")
        return True

    def get_balance(self, username):
        account = self.accounts.get(username)
        if account:
            print(f"Balance for {username}: {account['balance']}")
            return account['balance']
        else:
            print(f"Account for {username} not found.")
            return None

    def transfer_money(self, sender, receiver, amount):
        if sender not in self.accounts:
            print(f"Sender account {sender} not found.")
            return False
        if receiver not in self.accounts:
            print(f"Receiver account {receiver} not found.")
            return False
        if self.accounts[sender]['balance'] < amount:
            print(f"Insufficient funds for {sender}.")
            return False
        if amount <= 0:
            print("Transfer amount must be positive.")
            return False

        self.accounts[sender]['balance'] -= amount
        self.accounts[receiver]['balance'] += amount
        self.transaction_id_counter += 1
        transaction = {
            'id': self.transaction_id_counter,
            'sender': sender,
            'receiver': receiver,
            'amount': amount,
            'timestamp': time.time()
        }
        self.accounts[sender]['transactions'].append(transaction)
        self.accounts[receiver]['transactions'].append(transaction)
        print(f"Transferred {amount} from {sender} to {receiver}. Transaction ID: {self.transaction_id_counter}")
        return True

    def view_transactions(self, username):
        account = self.accounts.get(username)
        if account:
            print(f"\n--- Transactions for {username} ---")
            if not account['transactions']:
                print("No transactions yet.")
                return
            for tx in account['transactions']:
                print(f"ID: {tx['id']}, From: {tx['sender']}, To: {tx['receiver']}, Amount: {tx['amount']}")
            print("----------------------------------")
        else:
            print(f"Account for {username} not found.")

import time

if __name__ == "__main__":
    ps = PaymentSystem()
    print("--- Simple CLI Payment System ---")
    print("Commands: create <username> [balance], balance <username>, transfer <sender> <receiver> <amount>, transactions <username>, exit")

    while True:
        command_input = input("> ").split()
        cmd = command_input[0].lower()

        if cmd == "create":
            if len(command_input) >= 2:
                username = command_input[1]
                balance = int(command_input[2]) if len(command_input) == 3 else 0
                ps.create_account(username, balance)
            else:
                print("Usage: create <username> [balance]")
        elif cmd == "balance":
            if len(command_input) == 2:
                ps.get_balance(command_input[1])
            else:
                print("Usage: balance <username>")
        elif cmd == "transfer":
            if len(command_input) == 4:
                try:
                    sender = command_input[1]
                    receiver = command_input[2]
                    amount = float(command_input[3])
                    ps.transfer_money(sender, receiver, amount)
                except ValueError:
                    print("Invalid amount.")
            else:
                print("Usage: transfer <sender> <receiver> <amount>")
        elif cmd == "transactions":
            if len(command_input) == 2:
                ps.view_transactions(command_input[1])
            else:
                print("Usage: transactions <username>")
        elif cmd == "exit":
            print("Exiting Payment System.")
            break
        else:
            print("Unknown command.")
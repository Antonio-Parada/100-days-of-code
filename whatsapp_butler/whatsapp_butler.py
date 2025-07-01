import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

class WhatsAppButler:
    def __init__(self):
        self.reminders = []

    def scrape_wikipedia_summary(self, topic):
        try:
            response = requests.get(f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic}")
            data = response.json()
            return data.get('extract', 'No summary found.')
        except Exception as e:
            return f"Could not fetch Wikipedia summary: {e}"

    def add_reminder(self, name, date_str, message):
        try:
            event_date = datetime.strptime(date_str, '%Y-%m-%d')
            self.reminders.append({'name': name, 'date': event_date, 'message': message})
            return f"Reminder added for {name} on {date_str}."
        except ValueError:
            return "Invalid date format. Please use YYYY-MM-DD."

    def check_reminders(self):
        today = datetime.now().date()
        due_reminders = []
        for reminder in self.reminders:
            if reminder['date'].date() == today:
                due_reminders.append(reminder)
        return due_reminders

    def simulate_whatsapp_message(self, recipient, message):
        print(f"[WhatsApp Simulation] Sending to {recipient}: {message}")

if __name__ == "__main__":
    butler = WhatsAppButler()

    print("--- WhatsApp Butler Simulation ---")

    # Simulate scraping Wikipedia
    print("\nWikipedia Summary for 'Artificial Intelligence':")
    print(butler.scrape_wikipedia_summary("Artificial_Intelligence"))

    # Simulate adding and checking reminders
    butler.add_reminder("Alice's Birthday", "2025-07-01", "Happy Birthday, Alice!")
    butler.add_reminder("Project Deadline", "2025-07-05", "Don't forget the project deadline!")

    print("\nChecking reminders for today:")
    today_reminders = butler.check_reminders()
    if today_reminders:
        for reminder in today_reminders:
            butler.simulate_whatsapp_message(reminder['name'], reminder['message'])
    else:
        print("No reminders for today.")

    print("\n--- End of Simulation ---")

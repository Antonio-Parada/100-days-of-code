class SurveyApp:
    def __init__(self):
        self.surveys = {}
        self.survey_id_counter = 0

    def create_survey(self, title, questions):
        self.survey_id_counter += 1
        survey_id = self.survey_id_counter
        self.surveys[survey_id] = {
            'title': title,
            'questions': questions, # List of dicts: {'text': 'Q', 'type': 'multiple_choice', 'options': [...]} or {'type': 'open_ended'}
            'responses': []
        }
        print(f"Survey '{title}' created with ID {survey_id}.")
        return survey_id

    def take_survey(self, survey_id):
        if survey_id not in self.surveys:
            print(f"Survey with ID {survey_id} not found.")
            return

        survey = self.surveys[survey_id]
        print(f"\n--- Taking Survey: {survey['title']} ---")
        current_response = {}

        for i, q in enumerate(survey['questions']):
            print(f"\nQuestion {i+1}: {q['text']}")
            if q['type'] == 'multiple_choice':
                for j, option in enumerate(q['options']):
                    print(f"{j+1}. {option}")
                while True:
                    try:
                        choice = int(input("Enter your choice: "))
                        if 1 <= choice <= len(q['options']):
                            current_response[q['text']] = q['options'][choice-1]
                            break
                        else:
                            print("Invalid choice.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
            elif q['type'] == 'open_ended':
                answer = input("Your answer: ")
                current_response[q['text']] = answer
        
        survey['responses'].append(current_response)
        print("Survey completed. Thank you for your response!")

    def view_responses(self, survey_id):
        if survey_id not in self.surveys:
            print(f"Survey with ID {survey_id} not found.")
            return

        survey = self.surveys[survey_id]
        print(f"\n--- Responses for Survey: {survey['title']} ---")
        if not survey['responses']:
            print("No responses yet.")
            return

        for i, response in enumerate(survey['responses']):
            print(f"\nResponse {i+1}:")
            for q_text, answer in response.items():
                print(f"  {q_text}: {answer}")
        print("----------------------------------")

if __name__ == "__main__":
    app = SurveyApp()

    # Create a sample survey
    sample_questions = [
        {'text': 'What is your favorite color?', 'type': 'multiple_choice', 'options': ['Red', 'Blue', 'Green']},
        {'text': 'Any additional comments?', 'type': 'open_ended'}
    ]
    survey_id = app.create_survey("Customer Feedback", sample_questions)

    while True:
        print("\nCommands: take <survey_id>, view <survey_id>, exit")
        command_input = input("> ").split()
        cmd = command_input[0].lower()

        if cmd == "take":
            if len(command_input) == 2:
                try:
                    app.take_survey(int(command_input[1]))
                except ValueError:
                    print("Invalid survey ID.")
            else:
                print("Usage: take <survey_id>")
        elif cmd == "view":
            if len(command_input) == 2:
                try:
                    app.view_responses(int(command_input[1]))
                except ValueError:
                    print("Invalid survey ID.")
            else:
                print("Usage: view <survey_id>")
        elif cmd == "exit":
            print("Exiting Survey App.")
            break
        else:
            print("Unknown command.")

class VirtualAssistant:
    def __init__(self):
        self.todo_list = []
        self.notes = {}
        self.note_id_counter = 0

    def process_command(self, command):
        command_lower = command.lower()

        if "add todo" in command_lower:
            task = command.replace("add todo", "").strip()
            if task:
                self.todo_list.append(task)
                return f"Added to todo list: {task}"
            return "Please specify a task to add."
        
        elif "show todo" in command_lower:
            if self.todo_list:
                response = "Your todo list:\n"
                for i, task in enumerate(self.todo_list):
                    response += f"{i+1}. {task}\n"
                return response
            return "Your todo list is empty."

        elif "add note" in command_lower:
            note_content = command.replace("add note", "").strip()
            if note_content:
                self.note_id_counter += 1
                self.notes[self.note_id_counter] = note_content
                return f"Note added with ID {self.note_id_counter}."
            return "Please specify content for the note."

        elif "show note" in command_lower:
            try:
                note_id = int(command_lower.replace("show note", "").strip())
                if note_id in self.notes:
                    return f"Note {note_id}: {self.notes[note_id]}"
                return f"Note with ID {note_id} not found."
            except ValueError:
                return "Please specify a valid note ID (e.g., 'show note 1')."

        elif "hello" in command_lower or "hi" in command_lower:
            return "Hello! How can I assist you?"

        elif "exit" in command_lower or "bye" in command_lower:
            return "Goodbye!"

        else:
            return "I'm sorry, I don't understand that command."

if __name__ == "__main__":
    assistant = VirtualAssistant()
    print("--- Simple CLI Virtual Assistant ---")
    print("Commands: add todo <task>, show todo, add note <content>, show note <id>, hello/hi, exit/bye")

    while True:
        user_input = input("You: ")
        response = assistant.process_command(user_input)
        print(f"Assistant: {response}")
        if "goodbye" in response.lower():
            break
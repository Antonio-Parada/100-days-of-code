class ApplicationBuilder:
    def __init__(self):
        self.ui_elements = []

    def parse_description(self, description):
        lines = description.strip().split('
')
        for line in lines:
            line = line.strip()
            if not line:
                continue

            parts = line.split(':', 1)
            if len(parts) == 2:
                element_type = parts[0].strip().lower()
                properties_str = parts[1].strip()

                properties = {}
                for prop_pair in properties_str.split(','):
                    if '=' in prop_pair:
                        key, value = prop_pair.split('=', 1)
                        properties[key.strip()] = value.strip()
                
                self.ui_elements.append({'type': element_type, 'properties': properties})
            else:
                print(f"Warning: Could not parse line: {line}")

    def generate_ui_representation(self):
        print("\n--- Generated UI Representation ---")
        if not self.ui_elements:
            print("No UI elements defined.")
            return

        for element in self.ui_elements:
            print(f"Type: {element['type'].capitalize()}")
            for key, value in element['properties'].items():
                print(f"  {key.capitalize()}: {value}")
            print("----------------------------------")

if __name__ == "__main__":
    builder = ApplicationBuilder()

    app_description = """
    Button: text=Click Me, id=myButton, color=blue
    Label: text=Welcome to my App, font_size=24
    Input: placeholder=Enter your name, type=text
    """

    print("Parsing application description...")
    builder.parse_description(app_description)
    builder.generate_ui_representation()

    print("\n--- End of Simulation ---")

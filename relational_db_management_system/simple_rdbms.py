class SimpleRDBMS:
    def __init__(self):
        self.databases = {}
        self.current_db = None

    def create_database(self, db_name):
        if db_name in self.databases:
            print(f"Database '{db_name}' already exists.")
            return False
        self.databases[db_name] = {}
        print(f"Database '{db_name}' created.")
        return True

    def use_database(self, db_name):
        if db_name in self.databases:
            self.current_db = db_name
            print(f"Using database '{db_name}'.")
            return True
        else:
            print(f"Database '{db_name}' not found.")
            return False

    def create_table(self, table_name, columns):
        if not self.current_db:
            print("No database selected. Use 'use <db_name>' first.")
            return False
        if table_name in self.databases[self.current_db]:
            print(f"Table '{table_name}' already exists in '{self.current_db}'.")
            return False
        
        self.databases[self.current_db][table_name] = {
            'columns': columns, # List of column names
            'data': [] # List of dictionaries, each dict is a row
        }
        print(f"Table '{table_name}' created in '{self.current_db}'. Columns: {columns}")
        return True

    def insert_into_table(self, table_name, row_data):
        if not self.current_db:
            print("No database selected.")
            return False
        if table_name not in self.databases[self.current_db]:
            print(f"Table '{table_name}' not found in '{self.current_db}'.")
            return False
        
        table = self.databases[self.current_db][table_name]
        if set(row_data.keys()) != set(table['columns']):
            print("Column mismatch. Please provide data for all defined columns.")
            return False

        table['data'].append(row_data)
        print(f"Row inserted into '{table_name}'.")
        return True

    def select_from_table(self, table_name, conditions=None):
        if not self.current_db:
            print("No database selected.")
            return []
        if table_name not in self.databases[self.current_db]:
            print(f"Table '{table_name}' not found in '{self.current_db}'.")
            return []

        table = self.databases[self.current_db][table_name]
        results = []
        for row in table['data']:
            match = True
            if conditions:
                for col, val in conditions.items():
                    if row.get(col) != val:
                        match = False
                        break
            if match:
                results.append(row)
        return results

if __name__ == "__main__":
    rdbms = SimpleRDBMS()
    print("--- Simple CLI RDBMS Simulation ---")
    print("Commands: create_db <name>, use_db <name>, create_table <name> <col1,col2,...>, insert <table_name> <col1=val1,col2=val2,...>, select <table_name> [col=val], exit")

    while True:
        command_input = input("> ").split(maxsplit=1)
        cmd = command_input[0].lower()

        if cmd == "create_db":
            if len(command_input) == 2:
                rdbms.create_database(command_input[1])
            else:
                print("Usage: create_db <name>")
        elif cmd == "use_db":
            if len(command_input) == 2:
                rdbms.use_database(command_input[1])
            else:
                print("Usage: use_db <name>")
        elif cmd == "create_table":
            if len(command_input) == 2:
                parts = command_input[1].split(' ', 1)
                if len(parts) == 2:
                    table_name = parts[0]
                    columns = [c.strip() for c in parts[1].split(',')]
                    rdbms.create_table(table_name, columns)
                else:
                    print("Usage: create_table <name> <col1,col2,...>")
            else:
                print("Usage: create_table <name> <col1,col2,...>")
        elif cmd == "insert":
            if len(command_input) == 2:
                parts = command_input[1].split(' ', 1)
                if len(parts) == 2:
                    table_name = parts[0]
                    row_data = {}
                    for item in parts[1].split(','):
                        key_val = item.split('=', 1)
                        if len(key_val) == 2:
                            row_data[key_val[0].strip()] = key_val[1].strip()
                    rdbms.insert_into_table(table_name, row_data)
                else:
                    print("Usage: insert <table_name> <col1=val1,col2=val2,...>")
            else:
                print("Usage: insert <table_name> <col1=val1,col2=val2,...>")
        elif cmd == "select":
            if len(command_input) >= 2:
                parts = command_input[1].split(' ', 1)
                table_name = parts[0]
                conditions = None
                if len(parts) == 2:
                    cond_str = parts[1]
                    conditions = {}
                    for item in cond_str.split(','):
                        key_val = item.split('=', 1)
                        if len(key_val) == 2:
                            conditions[key_val[0].strip()] = key_val[1].strip()
                
                results = rdbms.select_from_table(table_name, conditions)
                print(f"\n--- Select Results from {table_name} ---")
                if results:
                    for row in results:
                        print(row)
                else:
                    print("No results found.")
                print("----------------------------------")
            else:
                print("Usage: select <table_name> [col=val]")
        elif cmd == "exit":
            print("Exiting RDBMS simulation.")
            break
        else:
            print("Unknown command.")

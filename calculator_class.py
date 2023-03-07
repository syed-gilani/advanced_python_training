class Calc:
    def __init__(self):
        self._math_ops = {
            "add": self.add,
            "subtract": self.subtract,
            "multiply": self.multiply,
            "divide": self.divide,
            "exponent": self.exponent,
        }
        self._calc_commands = ["add", "subtract", "multiply", "divide", "exponent"]
        self._result = 0

    def add(self, op_value1, op_value2):
        return op_value1 + op_value2

    def subtract(self, op_value1, op_value2):
        return op_value1 - op_value2
    
    def multiply(self, op_value1, op_value2):
        return op_value1 * op_value2

    def divide(self, op_value1, op_value2):
        return op_value1 / op_value2

    def exponent(self, op_value1, op_value2):
        return op_value1 ** op_value2
    
    def is_valid_command(self, command):
        return command in self._calc_commands
    
    def calc_result(self, history):
        for entry in history:
            print(entry)
            self._result = self._math_ops[entry["opName"]](self._result, entry["opValue"])
            print(self._result)
        return self._result

class UserEntry:

    def get_command(self):
        return input("Enter a command:")

    def get_operand(self):
        return float(input("Please enter an operand:"))

    def get_history_entry_id(self, prompt = None):
        if prompt:
            return int(input(prompt))
        else:
            return int(input("Please enter the history entry id: "))

class History:

    def __init__(self):
        self._history = []

    def get_history(self):
        return self._history

    def command_show_history(self):
        print(self._history)

    def command_clear_history(self):
        self._history.clear()

    def get_next_id(self):
        next_id = 1
        if self._history:
            next_id = max([ entry["id"] for entry in self._history ]) + 1
        return next_id

    def command_add_history_entry(self, entry_id, op_name, op_value):
        self._history.append({
            "id": entry_id,
            "opName": op_name,
            "opValue": op_value
        })

    def command_remove_history_entry(self, history_entry_id):
        for entry in self._history:
            if entry["id"] == history_entry_id:
                history.remove(entry)
                break
calc = Calc()
history = History()
user_entry = UserEntry()

while True:
    command = user_entry.get_command()
    if calc.is_valid_command(command):
        operand = user_entry.get_operand()
        history.command_add_history_entry(
            history.get_next_id(), command, operand)
        #print(calc.calc_result(history.get_history()))   
    elif command == "remove":
        history_entry_id = user_entry.get_history_entry_id()
        history.command_remove_history_entry(history_entry_id)
    elif command == "clear":
        history.command_clear_history()
    elif command == "history":
        history.command_show_history()
    elif command == "exit":
        break
    else:
        print("Invalid Command, Try Again")
        continue
result = calc.calc_result(history.get_history())
print(result)

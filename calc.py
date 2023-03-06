
history = []

def print_history(history):
    for command in history:
        print(f"ID: {command['id']}, Operator: {command['opName']}, Operand: {command['opValue']}")

def get_history_id(history):
    next_id = 1
    if history:
        next_id = max([ entry["id"] for entry in history ]) + 1
    return next_id

def add_command_to_history(next_id, command, operand):
    history.append({
            "id": next_id,
            "opName": command,
            "opValue": operand
        })

def compute_result(history):
    print(history)
    result = 0.0 if history[0]['opName'] in ['add','subtract'] else 1.0
    for item in history:
        if item['opName'] == 'add':
            result = result + item['opValue']
        elif item['opName'] == 'subtract':
            result = result - item['opValue']
        elif item['opName'] == 'multiply':
            result = result * item['opValue']
        elif item['opName'] == 'divide':
            result = result / item['opValue']
        elif item['opName'] == 'exponent':
            result = result ** item['opValue']
    return result


while True:

    command = input("Enter a command:")
    result = 0.0

    if command == "add":

        operand = float(input("Please enter an operand:"))
        result = result + operand

        next_id = get_history_id(history)

        add_command_to_history(next_id, "add", operand)    

        print(result)   


    elif command == "subtract":

        operand = float(input("Please enter an operand:"))
        result = result - operand

        next_id = get_history_id(history)
        add_command_to_history(next_id, "subtract", operand)        

        print(result)   


    elif command == "multiply":

        operand = float(input("Please enter an operand:"))
        result = result * operand

        next_id = get_history_id(history)

        add_command_to_history(next_id, "multiply", operand)

        print(result)   
      

    elif command == "divide":

        operand = float(input("Please enter an operand:"))
        result = result / operand

        next_id = get_history_id(history)

        add_command_to_history(next_id, "divide", operand)

        print(result)   

    elif command == "exponent":

        operand = float(input("Please enter an operand:"))
        result = result ** operand

        next_id = get_history_id(history)

        add_command_to_history(next_id, "exponent", operand)

        print(result)
    
    elif command == "history":
        next_id = 1
        if history:
            next_id = max([ entry["id"] for entry in history ]) + 1
        print_history(history)

    elif command == "remove":
        command_id = int(input('Enter command ID to remove commmand'))
        item_index = next((i for i, item in enumerate(history) if item["id"] == command_id), None)
        if item_index:
            del history[item_index]
        else:
            print(f'ID {command_id} does not exist')

    elif command == 'clear':
        history = []

    elif command == "exit":
        break
    else:
        print("Invalid Command, Try Again")
        continue
result = compute_result(history)
print(result)


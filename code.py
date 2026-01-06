History_File = "history.txt"

def history_show():
    file = open(History_File, "r")
    line = file.readline()
    if len(line) == 0:
        print("No history found.")
    else:
        for line in reversed(file.readlines()):
            print(line.strip())
    file.close()

def clear_history():
    file = open(History_File, "w")
    file.close()
    print("History cleared.")
    file.close()

def save_history(equation, result):
    file = open(History_File, "a")
    file.write(equation + " = " + str(result) + "\n")
    file.close()

def calculate(user_input):
    part = user_input.split()
    if len(part) != 3:
        print("Invalid input. Use: number operator number (e.g., 8 + 8)")
        return
    
    num1 = float(part[0])
    operator = part[1]
    num2 = float(part[2])

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            return
        result = num1 / num2
    else:
        print("Invalid operator. Use +, -, *, or /.")
        return
    if int(result) == result:
        result = int(result)
    print("Result:", result)
    save_history(user_input, result)

def main():
    print("------Simple Calculator! with (Type: history, clear, or quit)------")
    while True:
        user_input = input("Enter calculation (+, -, *, /) or command (history, clear, quit or exit) ")
        if user_input.lower() == "exit" or user_input.lower() == "quit":
            print("Exiting calculator. Goodbye!")
            break
        elif user_input.lower() == "history":
            history_show()
        elif user_input.lower() == "clear":
            clear_history()
        else:
            calculate(user_input)
main()

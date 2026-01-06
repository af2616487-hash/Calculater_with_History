# Calculator with History

A simple command-line **calculator** built in Python that performs basic arithmetic operations and stores each calculation in a history file so the user can view or clear past operations.

---

## Project overview

This project provides a text-based interface where users can perform basic mathematical operations (addition, subtraction, multiplication, division). Each successful calculation is stored in a `history.txt` file, and users can view or clear this calculation history using simple commands.

---

## Features

- Perform basic operations: `+`, `-`, `*`, `/`.
- Accept input in the format: `number operator number` (for example: `8 + 2`).
- Save every calculation to a `history.txt` file.
- View previous calculations using the `history` command.
- Clear all stored calculations using the `clear` command.
- Exit the program using `quit` or `exit`.

---

## Concepts used

| Concept              | Where it is used                                             | Why it is used                                                                 |
|----------------------|--------------------------------------------------------------|--------------------------------------------------------------------------------||
| Functions            | `history_show`, `clear_history`, `save_history`, `calculate`, `main` | To keep code modular, readable, and easy to maintain. |
| File handling        | `history_show`, `clear_history`, `save_history`             | To store, read, and clear the history of calculations in `history.txt`. |
| While loop           | `main`                                                      | To continuously accept user input until the user chooses to exit. |
| Conditional logic    | `calculate`, `main`                                         | To select between commands (`history`, `clear`, `quit`) and operators. |
| String processing    | `calculate`                                                 | To split user input into operands and operator using `split()`. |
| Type conversion      | `calculate`                                                 | To convert the string input into numeric (`float`) values for arithmetic. |
| Basic error handling | `calculate`, `history_show`                                 | To handle invalid input, division by zero, and empty history situations. |

---

## How the logic works

1. The program starts in the `main()` function and prints a welcome message.
2. An infinite loop (`while True`) runs to continuously take user input.
3. The user can enter either:
   - A **command**:
     - `history` → show saved calculations from `history.txt`.
     - `clear` → delete all stored history.
     - `quit` or `exit` → stop the loop and end the program.
   - Or a **mathematical expression**:
     - Example: `8 + 8`, `10 / 4`, `5 * 3`.

4. For expressions, `main()` sends the input string to `calculate(user_input)`.
5. Inside `calculate()`:
   - The input is split into three parts: first number, operator, second number.
   - If the format is not correct (not exactly 3 parts), an error message is printed.
   - Both numbers are converted to `float`.
   - Based on the operator (`+`, `-`, `*`, `/`), the corresponding arithmetic operation is performed.
   - Division by zero is checked and handled with a specific error message.
   - If the result is a whole number, it is converted to `int` for cleaner output.
   - The result is printed to the terminal.
   - `save_history()` is called to append a line like `8 + 8 = 16` to `history.txt`.

6. When the user inputs `history`, the `history_show()` function reads `history.txt` and prints previously stored calculations (or a message if no history exists).
7. When the user inputs `clear`, the `clear_history()` function empties `history.txt`, resetting the history.

---

## Pseudocode

```
SET HISTORY_FILE = "history.txt"

FUNCTION history_show():
    TRY to open HISTORY_FILE in read mode
        READ all lines
        IF no lines:
            PRINT "No history found."
        ELSE:
            FOR each line:
                PRINT line (trimmed)
    IF file does not exist:
        PRINT "No history found."

FUNCTION clear_history():
    OPEN HISTORY_FILE in write mode
    CLOSE file (this clears its content)
    PRINT "History cleared."

FUNCTION save_history(equation, result):
    OPEN HISTORY_FILE in append mode
    WRITE equation + " = " + result + newline
    CLOSE file

FUNCTION calculate(user_input):
    SPLIT user_input by spaces INTO parts

    IF length(parts) != 3:
        PRINT "Invalid input. Use: number operator number"
        RETURN

    num1_text = parts[0]
    operator  = parts[1]
    num2_text = parts[2]

    CONVERT num1_text TO float -> num1
    CONVERT num2_text TO float -> num2

    IF operator == "+":
        result = num1 + num2
    ELSE IF operator == "-":
        result = num1 - num2
    ELSE IF operator == "*":
        result = num1 * num2
    ELSE IF operator == "/":
        IF num2 == 0:
            PRINT "Error: Cannot divide by zero."
            RETURN
        result = num1 / num2
    ELSE:
        PRINT "Invalid operator. Use +, -, *, or /."
        RETURN

    IF result is a whole number:
        CONVERT result TO integer

    PRINT "Result:", result
    CALL save_history(user_input, result)

FUNCTION main():
    PRINT "------ Simple Calculator with History ------"
    LOOP forever:
        PRINT "Enter calculation (+, -, *, /) or command (history, clear, quit, exit):"
        READ user_input

        IF user_input.lower() is "quit" or "exit":
            PRINT "Exiting calculator. Goodbye!"
            BREAK
        ELSE IF user_input.lower() is "history":
            CALL history_show()
        ELSE IF user_input.lower() is "clear":
            CALL clear_history()
        ELSE:
            CALL calculate(user_input)

CALL main()
```

---

## Example usage

- Input: `8 + 8`
  - Output: `Result: 16`
  - History file: `8 + 8 = 16`

- Input: `10 / 4`
  - Output: `Result: 2.5`
  - History file: `10 / 4 = 2.5`

- Input: `history`
  - Output: All previous calculations stored in `history.txt`.

- Input: `clear`
  - Output: `History cleared.` and `history.txt` becomes empty.

- Input: `10 / 0`
  - Output: `Error: Cannot divide by zero.`

---

## How to run

1. Make sure Python is installed on your system.
2. Clone this repository:
   ```
   git clone https://github.com/af2616487-hash/Calculater_with_History.git
   cd Calculater_with_History
   ```
3. Run the program:
   ```
   python code.py
   ```

---

## Project structure

```
Calculater_with_History/
├── code.py          (Main calculator application)
├── README.md        (Project documentation)
└── history.txt      (Auto-generated file for storing calculation history)
```

---

## Author

**af2616487-hash** - B.Tech CSE Student

## License

This project is open source and available under the MIT License.

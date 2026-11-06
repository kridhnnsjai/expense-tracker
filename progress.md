# Expense Tracker – Progress

## Current Stage
Stage 1 – Small Python Projects

## Session 1

### What I learned
- Using `print()` and `input()`.
- Storing user input in variables.
- Using f-strings.
- Using `if`, `elif` and `else`.
- Repeating code with `while` loops.
- Stopping loops with `break`.
- Basic Git and GitHub workflow.

### What I implemented
- Created the Expense Tracker project.
- Built an interactive terminal menu.
- Added menu options for adding expenses, viewing expenses and exiting.
- Added input handling and invalid-option handling.

### Problems encountered and solutions
- Learned that Git needs an initial commit before pushing.
- Resolved GitHub network and authentication issues.
- Understood local Git repositories and GitHub remotes.

### What I can now do independently
- Display a menu using print().
- Collect user input.
- Make decisions using conditions.
- Repeat a menu using while True.
- Stop a loop using break.

### Remaining Tasks
- Implement expense entry.
- Store expenses.
- Display saved expenses.
- Add file storage.
- Improve input validation.

### Next Session Starting Point
Build the Add Expense feature. Learn how to collect an expense name and amount, then store them using a Python dictionary.

## Session 2 – Expense Tracker Features

### Project
Terminal-based Python Expense Tracker.

### What I learned
- How to store multiple dictionaries inside a list.
- How to use `append()` to add items to a list.
- How to use `len()` to count list items.
- How to use `for` loops to display list items.
- How to convert input into numbers using `float()`.
- How to handle errors using `try`, `except`, and `ValueError`.
- How to validate input using conditions.
- How to use `.strip()` to remove extra spaces.

### What I implemented
- Add expenses with a name and amount.
- Store multiple expenses in a list of dictionaries.
- View all saved expenses.
- Calculate total spending.
- Reject empty expense names.
- Reject zero and negative amounts.
- Handle invalid amount input without crashing.

### Problems and solutions
- F-string quotation conflict: fixed dictionary key quotation marks.
- Expenses being replaced: used a list and `append()`.
- Text being entered as an amount: used `float()`.
- Invalid amount crashing the program: added `try` and `except`.
- Empty names and spaces: added validation and `.strip()`.

### What I can do independently
- Create and access dictionaries.
- Store dictionaries inside lists.
- Use loops to process collections.
- Calculate totals.
- Convert input into numbers.
- Handle invalid input.
- Build a menu-based terminal application.

### Remaining tasks
- Improve the project structure.
- Learn how to save expenses permanently using files.
- Add more useful expense-tracking features.

### Next session starting point
Continue the Expense Tracker project by learning file handling.
Start by explaining how Python can save and load expense data using JSON.

## Session 3 – JSON File Handling

### What I learned
- JSON data format.
- Reading and writing files with open().
- Read mode ("r") and write mode ("w").
- json.dump() and json.load().
- Handling FileNotFoundError.
- Handling JSONDecodeError.

### What I implemented
- Saving expenses to expenses.json.
- Loading expenses when the program starts.
- Keeping expenses after restarting the application.
- Handling missing or invalid JSON files.

### Next session
Improve the application structure and learn Python functions.

## Session 4 - Functions 
- Created view_expenses(), calculate_total(), and add_expense().
- Learned function definitions and function calls.
- Learned parameters and arguments.
- Understood the difference between print() and return.
- Practised using len() with a function parameter.

## Session 5 – Python Modules

### What I learned
- What Python modules are.
- How to import functions using `from ... import`.
- How to pass data between modules using parameters.
- How to organize code across multiple Python files.
- How `if __name__ == "__main__":` works.

### What I implemented
- Created `expense_views.py` for viewing expenses and calculating totals.
- Created `expense_operations.py` for adding and saving expenses.
- Updated `main.py` to import and use functions from other modules.
- Added the main execution condition.

### New concepts
- Modules
- Imports
- `__name__`
- `__main__`

### Testing
- Adding expenses: Passed
- Viewing expenses: Passed
- Calculating total: Passed
- JSON persistence: Passed

### Next session
Learn about Python packages and better project organization.

## Session 6 - Python Packages

### What I learned
- A module is a Python file.
- A package is a folder that organizes related Python modules.
- `__init__.py` marks a regular Python package.
- How to import functions from modules inside a package.

### What I implemented
- Created an `expenses` package.
- Created `__init__.py`.
- Moved `expense_views.py` and `expense_operations.py` into the package.
- Updated imports in `main.py`.
- Tested the application after reorganizing the files.

### New concepts
- Python packages
- Package import paths
- Organizing project files

### What I can do independently
- Create a Python package.
- Move modules into a package.
- Import functions from modules inside a package.

### Remaining tasks
- Review project structure.
- Learn how to keep project files organized.
- Continue with the next Python topic.

### Next session starting point
- Review Python packages and imports.
- Begin the next stage of Python development.

## Session 7 - Virtual Environments and pip

### What I learned
- What virtual environments are and why developers use them.
- How to create and activate a virtual environment.
- How to use pip to install Python packages.
- Difference between built-in modules and external packages.
- What package dependencies are.
- How requirements.txt records project dependencies.

### What I implemented
- Created and activated .venv.
- Installed requests.
- Created requirements.txt using pip freeze.
- Updated .gitignore to exclude .venv.

### New concepts
- Virtual environments
- pip
- External packages
- Dependencies
- requirements.txt

### What I can do independently
- Create and activate a virtual environment.
- Install and inspect Python packages.
- Generate requirements.txt.
- Install dependencies using requirements.txt.

### Remaining tasks
- Learn how to use external libraries in Python projects.
- Continue learning APIs and backend development.

### Next session starting point
- Learn how to use the requests library.
- Understand HTTP requests and responses.

## Session 8 - Working with APIs

### What I learned
- What APIs are and how applications communicate.
- HTTP GET requests.
- HTTP status codes.
- Converting JSON responses into Python dictionaries.
- Accessing API response data.
- Handling unsuccessful HTTP responses.
- Handling connection errors using try/except.
- Using request timeouts.

### What I implemented
- Created api_practice.py.
- Sent GET requests using the requests library.
- Retrieved and displayed Todo information.
- Built a Todo Viewer using user input.
- Added HTTP error handling and connection error handling.

### New concepts
- APIs
- HTTP
- GET requests
- HTTP status codes
- JSON responses
- Request exceptions
- API timeouts

### What I can do independently
- Send basic GET requests.
- Read JSON responses.
- Access response data using dictionary keys.
- Check HTTP status codes.
- Handle request-related exceptions.
- Build dynamic API URLs.

### Remaining tasks
- Learn POST, PUT and DELETE requests.
- Learn API input validation.
- Understand API response structures.
- Practice working with external APIs.

### Next session starting point
- Learn how to send data to an API using POST.
- Understand the difference between GET and POST.
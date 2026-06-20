import os
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# This is the name of our paper notebook file on your computer
DATA_FILE = "tasks.txt"

def read_local_tasks():
    """Helper function: Tells the Chef to read the notebook file."""
    # If the file doesn't exist yet, return an empty list
    if not os.path.exists(DATA_FILE):
        return []
        
    with open(DATA_FILE, "r") as file:
        # Read every line, clean up extra spaces, and ignore empty lines
        return [line.strip() for line in file.readlines() if line.strip()]

def append_local_task(task_text):
    """Helper function: Tells the Chef to write a new line in the notebook."""
    with open(DATA_FILE, "a") as file:
        file.write(task_text + "\n")


@app.route('/')
def home():
    """Job 1: Showing the webpage to the user."""
    # The Chef reads the notebook...
    current_tasks = read_local_tasks()
    # ...and hands the list to the Waiter (HTML) to display on your screen
    return render_template('index.html', tasks=current_tasks)


@app.route('/add', methods=['POST'])
def add_task():
    """Job 2: Adding a brand new task."""
    # Grab the text that the user typed into the input box
    new_task = request.form.get('task_input')
    if new_task:
        # Write it down in our notebook file
        append_local_task(new_task)
    # Go back to the homepage to show the updated list
    return redirect('/')


@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    """Job 3: Erasing a task using its line number."""
    # 1. Read all the current tasks from our file
    current_tasks = read_local_tasks()
    
    # 2. Double-check that the line number actually exists
    if 0 <= task_id < len(current_tasks):
        # 3. Zap the task out of the list using Python's eraser (.pop)
        current_tasks.pop(task_id)
        
    # 4. Open the notebook with "w" to clear it out completely,
    # and rewrite only the tasks that weren't deleted.
    with open(DATA_FILE, "w") as file:
        for task in current_tasks:
            file.write(task + "\n")
            
    # 5. Go back to the homepage to show the fresh list
    return redirect('/')


if __name__ == '__main__':
    # This turns on our restaurant server!
    app.run(debug=True)
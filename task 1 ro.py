import tkinter as tk
from tkinter import messagebox
import json
import os

TODO_FILE = "todo.json"


def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

tasks = load_tasks()

def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append({"task": task, "completed": False})
        update_task_listbox()
        save_tasks(tasks)  
        
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def update_task_listbox():
    task_listbox.delete(0, tk.END)
    for i, task in enumerate(tasks):
        status = "Completed" if task["completed"] else "Pending"
        task_listbox.insert(tk.END, f"{i + 1}. {task['task']} [{status}]")

def delete_task():
    try:
        task_index = task_listbox.curselection()[0]
        tasks.pop(task_index)
        update_task_listbox()
        save_tasks(tasks)  
        
    except:
        messagebox.showwarning("Selection Error", "Please select a task.")

def toggle_task_completion():
    try:
        task_index = task_listbox.curselection()[0]
        tasks[task_index]["completed"] = not tasks[task_index]["completed"]
        update_task_listbox()
        save_tasks(tasks)  
    except:
        messagebox.showwarning("Selection Error", "Please select a task.")

app = tk.Tk()
app.title("To-Do List App")


app.config(bg="#DDEEFF")  


task_entry = tk.Entry(app, width=40, bg="#FFFFFF")  
task_entry.pack(pady=10)

add_button = tk.Button(app, text="Add Task", width=30, command=add_task, bg="#B3E5FC")  
add_button.pack(pady=5)

task_listbox = tk.Listbox(app, height=10, width=50, bg="#FFFFFF")  
task_listbox.pack(pady=10)

delete_button = tk.Button(app, text="Delete Task", width=30, command=delete_task, bg="#FFCDD2")  
delete_button.pack(pady=5)

toggle_button = tk.Button(app, text="Mark as Complete/Incomplete", width=30, command=toggle_task_completion, bg="#C8E6C9")  
toggle_button.pack(pady=5)

update_task_listbox() 

app.geometry("400x400")  
app.mainloop()
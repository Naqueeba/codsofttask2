import tkinter as tk

def add_task():
    task_name = task_entry.get()
    if task_name:
        task_listbox.insert(tk.END, task_name)
        task_entry.delete(0, tk.END)

def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.delete(selected_task)

root = tk.Tk()
root.title("To-Do List")

task_entry = tk.Entry(root)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

task_listbox = tk.Listbox(root)
task_listbox.pack()

root.mainloop()

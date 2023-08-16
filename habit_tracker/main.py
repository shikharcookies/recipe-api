import tkinter as tk
from tkinter import messagebox
import os

def save_habits(habits):
    with open("habits.txt", "w") as file:
        for habit in habits:
            file.write(habit + "\n")

def load_habits():
    habits = []
    if os.path.exists("habits.txt"):
        with open("habits.txt", "r") as file:
            habits = [line.strip() for line in file]
    return habits

def add_habit():
    habit = entry.get()
    if habit:
        habits.append(habit)
        listbox.insert(tk.END, habit)
        entry.delete(0, tk.END)
        save_habits(habits)
    else:
        messagebox.showwarning("Warning", "Please enter a habit!")

def remove_habit():
    selected_index = listbox.curselection()
    if selected_index:
        index = selected_index[0]
        habit = listbox.get(index)
        listbox.delete(index)
        habits.remove(habit)
        save_habits(habits)

def celebrate():
    messagebox.showinfo("Congratulations!", "Congratulations on completing today's habits!")

def track_progress():
    celebrate()

def create_ui(habits):
    root = tk.Tk()
    root.title("Habit Tracker")

    frame = tk.Frame(root)
    frame.pack(pady=10)

    global entry, listbox
    entry = tk.Entry(frame, width=30)
    entry.grid(row=0, column=0, padx=5)

    add_button = tk.Button(frame, text="Add Habit", command=add_habit)
    add_button.grid(row=0, column=1, padx=5)

    remove_button = tk.Button(frame, text="Remove Habit", command=remove_habit)
    remove_button.grid(row=0, column=2, padx=5)

    listbox_frame = tk.Frame(root)
    listbox_frame.pack(pady=10)

    listbox = tk.Listbox(listbox_frame, width=50)
    listbox.pack()

    for habit in habits:
        listbox.insert(tk.END, habit)

    track_button = tk.Button(root, text="Track Progress", command=track_progress)
    track_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    habits = load_habits()
    create_ui(habits)

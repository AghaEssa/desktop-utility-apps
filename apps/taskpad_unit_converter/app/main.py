import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# functions of unit converters
def convert():
    try:
        val = float(entry.get())
        ct = conversion_type.get()
        direction = conversion_direction.get()

        if ct == "Length":
            if direction == "Km to Miles":
                result = f"{val} kilometers = {round(val * 0.6214, 2)} miles"
            else:
                result = f"{val} miles = {round(val / 0.6214, 2)} kilometers"

        elif ct == "Weight":
            if direction == "Kg to Pounds":
                result = f"{val} kilograms = {round(val * 2.2046, 2)} pounds"
            else:
                result = f"{val} pounds = {round(val / 2.2046, 2)} kilograms"

        elif ct == "Temperature":
            if direction == "C to F":
                result = f"{val}°C = {round((val * 9/5) + 32, 2)}°F"
            else:
                result = f"{val}°F = {round((val - 32) * 5/9, 2)}°C"

        result_label.configure(text=result)
        # Show only current result
        result_box.delete("1.0", "end")
        result_box.insert("end", result)

    except Exception:
        result_label.configure(text="Please enter a valid number.")
        result_box.delete("1.0", "end")
        result_box.insert("end", "Invalid input")



def update_direction(event=None):
    ct = conversion_type.get()
    if ct == "Length":
        direction_menu.configure(values=["Km to Miles", "Miles to Km"])
        conversion_direction.set("Km to Miles")
    elif ct == "Weight":
        direction_menu.configure(values=["Kg to Pounds", "Pounds to Kg"])
        conversion_direction.set("Kg to Pounds")
    elif ct == "Temperature":
        direction_menu.configure(values=["C to F", "F to C"])
        conversion_direction.set("C to F")

# Functions_of_todo_list
def add_task():
    task = task_entry.get().strip()
    if task:
        task_listbox.insert("end", task + "\n")
        task_entry.delete(0, "end")
    else:
        messagebox.showwarning("Empty Field", "Please enter a task.")




# Global variable to store selected line index
selected_line_index = [None]

def on_task_click(event):
    # Remove previous highlight
    task_listbox.tag_remove("highlight", "1.0", "end")
    # Get clicked line index
    index = task_listbox.index(f"@{event.x},{event.y}").split(".")[0]
    selected_line_index[0] = int(index)
    # Highlight the clicked line
    task_listbox.tag_add("highlight", f"{index}.0", f"{index}.end")
    task_listbox.tag_config("highlight", background="#444444")  # Change color as needed









def delete_task():
    index = selected_line_index[0]
    if index is not None:
        lines = task_listbox.get("1.0", "end-1c").split("\n")
        if 1 <= index <= len(lines):
            del lines[index-1]
            task_listbox.delete("1.0", "end")
            for line in lines:
                task_listbox.insert("end", line + "\n")
            # Remove highlight after delete
            task_listbox.tag_remove("highlight", "1.0", "end")
            selected_line_index[0] = None
        else:
            messagebox.showwarning("No Selection", "No task selected.")
    else:
        messagebox.showwarning("No Selection", "Click a task to select it before deleting.")


def clear_all():
    if messagebox.askyesno("Clear All", "Are you sure you want to delete all tasks?"):
        task_listbox.delete("1.0", "end")

# main working_for all
root = ctk.CTk()
root.title("Unit Converter_By_Agha")
root.geometry("350x600")

# unit _converter
ctk.CTkLabel(root, text="Unit Converter", font=("Arial", 20, "bold")).pack(pady=10)

conversion_type = ctk.StringVar(value="Length")
conversion_dropdown = ctk.CTkComboBox(root, variable=conversion_type, values=["Length", "Weight", "Temperature"], font=("Arial", 14), width=200, command=update_direction)
conversion_dropdown.set("Length")
conversion_dropdown.pack(pady=5)

conversion_direction = ctk.StringVar(value="Km to Miles")
direction_menu = ctk.CTkComboBox(root, variable=conversion_direction, values=["Km to Miles", "Miles to Km"], font=("Arial", 14), width=200)
direction_menu.set("Km to Miles")
direction_menu.pack(pady=5)

entry = ctk.CTkEntry(root, font=("Arial", 14), width=180)
entry.pack(pady=10)

convert_btn = ctk.CTkButton(root, text="Convert", font=("Arial", 14), fg_color="#4caf50", text_color="white", width=180, command=convert)
convert_btn.pack(pady=10)

result_label = ctk.CTkLabel(root, text="", font=("Arial", 14), text_color="#00e6e6")
result_label.pack(pady=10)

# Result box for conversion history
result_box = ctk.CTkTextbox(root, font=("Arial", 13), width=320, height=20)
result_box.pack(pady=5)

# -----------------todolist work
heading = ctk.CTkLabel(root, text="My Daily Tasks", font=("Arial", 20, "bold"))
heading.pack(pady=10)

# Single-line entry for adding tasks
task_entry = ctk.CTkEntry(root, font=("Arial", 14), width=250)
task_entry.pack(pady=10)

btn_frame = ctk.CTkFrame(root)
btn_frame.pack(pady=5)

# Multi-line textbox for showing all tasks
task_listbox = ctk.CTkTextbox(root, font=("Arial", 13), width=320, height=180)
task_listbox.pack(pady=10)
task_listbox.bind("<Button-1>", on_task_click)



add_btn = ctk.CTkButton(btn_frame, text="Add Task", font=("Arial", 12), fg_color="#76b5c5", text_color="white", width=90, command=add_task)
add_btn.grid(row=0, column=0, padx=5)

del_btn = ctk.CTkButton(btn_frame, text="Delete Task", font=("Arial", 12), fg_color="#e27d60", text_color="white", width=110, command=delete_task)
del_btn.grid(row=0, column=1, padx=5)

clear_btn = ctk.CTkButton(btn_frame, text="Clear All", font=("Arial", 12), fg_color="#c94c4c", text_color="white", width=90, command=clear_all)
clear_btn.grid(row=0, column=2, padx=5)

update_direction()
root.mainloop()
import tkinter as tk
from tkinter import messagebox
import datetime
import random
import string


def calculate_entry_bill(age):
    if age < 18:
        return 500, "Children pay Ksh 500 for entry"
    else:
        return 1500, "Adults pay Ksh 1500 for entry"


def calculate_total_cost(age, needs_drinks, needs_photos):
    entry_bill, entry_message = calculate_entry_bill(age)

    if needs_drinks.lower() == "y":
        entry_bill += 250 if age >= 18 else 100

    if needs_photos.lower() == "yes":
        entry_bill += 300 if age >= 18 else 100

    return entry_bill, entry_message


def generate_receipt(
    name,
    age,
    needs_drinks,
    needs_photos,
    favorite_game,
    shift,
    total_cost,
    ticket_number,
    current_time,
):
    receipt = f"""Receipt Details. Please make sure to preserve it when you come to the Show!
    Name: {name}
    Age: {age}
    Needs Photos: {needs_photos}
    Needs Drinks: {needs_drinks}
    Favorite Game: {favorite_game}
    Shift: {shift}
    Entry Bill: {total_cost[1]}
    Total Bill: {total_cost[0]}
    TICKET NO: {ticket_number}

    You were served by Caleb
    Receipt printed at: {current_time.strftime('%Y-%m-%d %H:%M')}
    """
    return receipt


def submit():
    name = name_entry.get()
    age = age_entry.get()
    needs_drinks = drinks_var.get()
    needs_photos = photos_var.get()
    favorite_game = game_entry.get()
    shift = shift_var.get()

    if not all([name, age, needs_drinks, needs_photos, favorite_game, shift]):
        messagebox.showwarning("Alert", "Please enter all fields.")
        return

    try:
        age = int(age)  # Convert age to an integer
    except ValueError:
        messagebox.showwarning("Alert", "Please enter a valid age.")
        return

    entry_bill, entry_message = calculate_entry_bill(age)

    messagebox.showinfo("Entry Bill", entry_message)

    total_cost = calculate_total_cost(age, needs_drinks, needs_photos)
    ticket_number = "".join(random.choices(string.ascii_uppercase + string.digits, k=8))
    current_time = datetime.datetime.now()

    receipt = generate_receipt(
        name,
        age,
        needs_drinks,
        needs_photos,
        favorite_game,
        shift,
        total_cost,
        ticket_number,
        current_time,
    )

    messagebox.showinfo("Receipt", receipt)

    # Clear entry fields after submission
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    drinks_var.set("N")
    photos_var.set("No")
    game_entry.delete(0, tk.END)
    shift_var.set("Day")


def refresh():
    # Clear entry fields without submitting
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    drinks_var.set("N")
    photos_var.set("No")
    game_entry.delete(0, tk.END)
    shift_var.set("Day")


# GUI setup
root = tk.Tk()
root.title("Merit Game Challenge")
root.geometry("400x300")  # Set the size of the window

# Labels and Entry Widgets
tk.Label(root, text="Name:").grid(row=0, column=0, sticky="e")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Age:").grid(row=1, column=0, sticky="e")
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1)

tk.Label(root, text="Do you want drinks? (Y/N):").grid(row=2, column=0, sticky="e")
drinks_var = tk.StringVar(value="Y")
drinks_entry = tk.Entry(root, textvariable=drinks_var)
drinks_entry.grid(row=2, column=1)

tk.Label(root, text="Do you want photos? (Yes/No):").grid(row=3, column=0, sticky="e")
photos_var = tk.StringVar(value="Yes")
photos_entry = tk.Entry(root, textvariable=photos_var)
photos_entry.grid(row=3, column=1)

tk.Label(root, text="Favorite Game:").grid(row=4, column=0, sticky="e")
game_entry = tk.Entry(root)
game_entry.grid(row=4, column=1)

tk.Label(root, text="Shift (Day/Night):").grid(row=5, column=0, sticky="e")
shift_var = tk.StringVar(value="Day")
shift_entry = tk.Entry(root, textvariable=shift_var)
shift_entry.grid(row=5, column=1)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=6, column=0, columnspan=2)

# Refresh Button
refresh_button = tk.Button(root, text="Refresh", command=refresh)
refresh_button.grid(row=7, column=0, columnspan=2)

# Run the GUI
root.mainloop()

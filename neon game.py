import tkinter as tk
import random

# -----------------------------
# WINDOW
# -----------------------------

root = tk.Tk()
root.title("MATRIX HACKER")
root.geometry("800x600")
root.configure(bg="black")

# -----------------------------
# CANVAS
# -----------------------------

canvas = tk.Canvas(
    root,
    width=800,
    height=600,
    bg="black",
    highlightthickness=0
)

canvas.pack()

# -----------------------------
# MATRIX CHARACTERS
# -----------------------------

characters = "01ABCDEFGHIJKLMNOPQRSTUVWXYZ#$%&@"

columns = 80
drops = [random.randint(-20, 0) for _ in range(columns)]


# -----------------------------
# MATRIX ANIMATION
# -----------------------------

def matrix_effect():

    canvas.delete("matrix")

    for i in range(columns):

        x = i * 10
        y = drops[i] * 10

        char = random.choice(characters)

        # Neon green Matrix text
        canvas.create_text(
            x,
            y,
            text=char,
            fill="#00ff41",
            font=("Courier New", 12, "bold"),
            tags="matrix"
        )

        drops[i] += 1

        # Reset when character reaches bottom
        if drops[i] * 10 > 600:

            if random.random() > 0.975:
                drops[i] = random.randint(-20, 0)

    root.after(50, matrix_effect)


# -----------------------------
# HACKER TITLE
# -----------------------------

title = canvas.create_text(
    400,
    250,
    text="MATRIX",
    fill="#00ff41",
    font=("Courier New", 55, "bold")
)


subtitle = canvas.create_text(
    400,
    320,
    text="SYSTEM ACCESS GRANTED",
    fill="#00ffff",
    font=("Courier New", 18, "bold")
)


# -----------------------------
# START
# -----------------------------

matrix_effect()

root.mainloop()

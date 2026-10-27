import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("450x570")
root.resizable(False, False)
root.configure(bg="#151525")

current_player = "X"
board = [""] * 9
buttons = []
game_over = False

score_x = 0
score_o = 0

BG_COLOR = "#151525"
BUTTON_COLOR = "#252540"
X_COLOR = "#00D9FF"
O_COLOR = "#FF4D8D"
TEXT_COLOR = "#FFFFFF"
def check_winner():
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] != "":
            return (a, b, c)

    return None

def update_score():
    score_label.config(
        text=f"Player X: {score_x}     Player O: {score_o}"
    )
def button_click(index):
    global current_player, game_over, score_x, score_o

    if board[index] != "" or game_over:
        return

    board[index] = current_player

    color = X_COLOR if current_player == "X" else O_COLOR

    buttons[index].config(
        text=current_player,
        fg=color,
        disabledforeground=color,
        state="disabled"
    )

    winning_cells = check_winner()

    if winning_cells:
        game_over = True

        for cell in winning_cells:
            buttons[cell].config(bg="#3A3A60")

        status_label.config(
            text=f"🎉 Player {current_player} Wins!",
            fg=color
        )

        if current_player == "X":
            score_x += 1
        else:
            score_o += 1

        update_score()

        messagebox.showinfo(
            "Game Over",
            f"Congratulations! Player {current_player} wins!"
        )

        return

    if "" not in board:
        game_over = True
        status_label.config(text="It's a Draw!", fg="#FFD166")

        messagebox.showinfo(
            "Game Over",
            "It's a draw! Great game!"
        )

        return

    current_player = "O" if current_player == "X" else "X"

    status_label.config(
        text=f"Player {current_player}'s Turn",
        fg=X_COLOR if current_player == "X" else O_COLOR
    )

def restart_game():
    global current_player, board, game_over

    current_player = "X"
    board = [""] * 9
    game_over = False

    for button in buttons:
        button.config(
            text="",
            state="normal",
            bg=BUTTON_COLOR,
            fg=TEXT_COLOR
        )

    status_label.config(
        text="Player X's Turn",
        fg=X_COLOR
    )


def reset_scores():
    global score_x, score_o

    score_x = 0
    score_o = 0

    update_score()
    restart_game()
title_label = tk.Label(
    root,
    text="TIC TAC TOE",
    font=("Arial", 25, "bold"),
    bg=BG_COLOR,
    fg=TEXT_COLOR
)
title_label.pack(pady=(20, 5))

score_label = tk.Label(
    root,
    text="Player X: 0     Player O: 0",
    font=("Arial", 12, "bold"),
    bg=BG_COLOR,
    fg="#FFD166"
)
score_label.pack(pady=8)


status_label = tk.Label(
    root,
    text="Player X's Turn",
    font=("Arial", 15, "bold"),
    bg=BG_COLOR,
    fg=X_COLOR
)
status_label.pack(pady=10)
game_frame = tk.Frame(root, bg=BG_COLOR)
game_frame.pack(pady=10)

for i in range(9):
    button = tk.Button(
        game_frame,
        text="",
        font=("Arial", 28, "bold"),
        width=4,
        height=2,
        bg=BUTTON_COLOR,
        fg=TEXT_COLOR,
        activebackground="#41416A",
        relief="flat",
        bd=0,
        cursor="hand2",
        command=lambda index=i: button_click(index)
    )

    button.grid(
        row=i // 3,
        column=i % 3,
        padx=5,
        pady=5
    )

    buttons.append(button)

restart_button = tk.Button(
    root,
    text="🔄  Play Again",
    font=("Arial", 12, "bold"),
    bg="#6C63FF",
    fg="white",
    activebackground="#554CE0",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=restart_game
)
restart_button.pack(fill="x", padx=65, pady=(15, 7), ipady=7)

reset_button = tk.Button(
    root,
    text="Reset Scores",
    font=("Arial", 10),
    bg=BG_COLOR,
    fg="#AAAAAA",
    activebackground=BG_COLOR,
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=reset_scores
)
reset_button.pack(pady=3)
root.mainloop()
```

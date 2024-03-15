import tkinter as tk

def main():
    #Create main window for application.
    root = tk.TK()
    root.title("AlphaWave- Trading Platform")

    #Background color.
    root.configure(bg='1a1a1a')

    #Calculate dimensions  for the window to be 80% of screen size.
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = int(screen_width * 0.8)
    height = int(screen_height * 0.8)

    #Center the window screen.
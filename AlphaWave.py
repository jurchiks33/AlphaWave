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
    x_offset = int((screen_width - width) / 2)
    y_offset = int((screen_height - height) / 2)

    #Set initial size and position of the window.
    root.geometry(f'{width}x{height}+{x_offset}+{y_offset}')


    #Tkinter event loop.
    root.mainloop()

if __name__ == "__main__":
    main()
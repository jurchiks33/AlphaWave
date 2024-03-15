import tkinter as tk

def main():
    #Create main window for application.
    root = tk.Tk()
    root.title("AlphaWave- Trading Platform")

    #Background color.
    root.configure(bg='#a9d08f')

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

    #Here coming frames for the pages.
    frame1 = tk.Frame(root, bg='#dae1f3', bd=2, relief='solid')
    frame2 = tk.Frame(root, bg='white', bd=2, relief='solid')


    #Place frames in layout.
    frame1.place(relx=0, rely=0, relwidth=0.25, relheight=0.6)
    frame2.place(relx=0.3, rely=0, relwidth=0.64, relheight=0.4)

    #Tkinter event loop.
    root.mainloop()

if __name__ == "__main__":
    main()
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
    frame1 = tk.Frame(root, bg='#dae1f3', bd=1, relief='solid')
    frame2 = tk.Frame(root, bg='#d9d9d9', bd=1, relief='solid')
    frame3 = tk.Frame(root, bg='#b0bac3', bd=0.5, relief='solid')
    frame4 = tk.Frame(root, bg='#b0bac3', bd=0.5, relief='solid')
    frame5 = tk.Frame(root, bg='#b0bac3', bd=0.5, relief='solid')
    frame6 = tk.Frame(root, bg='#b0bac3', bd=0.5, relief='solid')
    frame7 = tk.Frame(root, bg='#a5a5a5', bd=1, relief='solid')
    frame8 = tk.Frame(root, bg='#a6a6a6', bd=2, relief='solid')
    frame9 = tk.Frame(root, bg='white', bd=0.5, relief='solid')
    frame10 = tk.Frame(root, bg='white', bd=0.5, relief='solid')
    frame11 = tk.Frame(root, bg='white', bd=0.5, relief='solid')
    frame12 = tk.Frame(root, bg='white', bd=0.5, relief='solid')
    frame13 = tk.Frame(root, bg='white', bd=0.5, relief='solid')
    frame14 = tk.Frame(root, bg='white', bd=0.5, relief='solid')
    frame15 = tk.Frame(root, bg='white', bd=0.5, relief='solid')
    frame16 = tk.Frame(root, bg='white', bd=0.5, relief='solid')
    frame17 = tk.Frame(root, bg='white', bd=0.5, relief='solid')
    frame18 = tk.Frame(root, bg='white', bd=0.5, relief='solid')


    #Place frames in layout.
    frame1.place(relx=0, rely=0, relwidth=0.25, relheight=0.6)
    frame2.place(relx=0.3, rely=0, relwidth=0.64, relheight=0.4)
    frame3.place(relx=0.3, rely=0.40, relwidth=0.16, relheight=0.03)
    frame4.place(relx=0.46, rely=0.4, relwidth=0.16, relheight=0.03)
    frame5.place(relx=0.62, rely=0.4, relwidth=0.16, relheight=0.03)
    frame6.place(relx=0.78, rely=0.4, relwidth=0.16, relheight=0.03)
    frame7.place(relx=0, rely=0.67, relwidth=0.25, relheight=0.3)
    frame8.place(relx=0.3, rely=0.5, relwidth=0.5, relheight=0.36)
    frame9.place(relx=0.80, rely=0.5, relwidth=0.2, relheight=0.04)
    frame10.place(relx=0.80, rely=0.54, relwidth=0.2, relheight=0.04)
    frame11.place(relx=0.80, rely=0.58, relwidth=0.2, relheight=0.04)
    frame12.place(relx=0.80, rely=0.62, relwidth=0.2, relheight=0.04)
    frame13.place(relx=0.80, rely=0.66, relwidth=0.2, relheight=0.04)
    frame14.place(relx=0.80, rely=0.70, relwidth=0.2, relheight=0.04)
    frame15.place(relx=0.80, rely=0.74, relwidth=0.2, relheight=0.04)
    frame16.place(relx=0.80, rely=0.78, relwidth=0.2, relheight=0.04)
    frame17.place(relx=0.80, rely=0.82, relwidth=0.2, relheight=0.04)
    frame18.place(relx=0, rely=0.97, relwidth=0.142, relheight=0.035)

    #Tkinter event loop.
    root.mainloop()

if __name__ == "__main__":
    main()
import tkinter as tk

class App:
    def __init__(self, master):
        self.master = master
        master.title("Squares")

        # Create the squares
        square1 = tk.Canvas(master, width=250, height=250, bg="red")
        square2 = tk.Canvas(master, width=250, height=250, bg="green")
        square3 = tk.Canvas(master, width=250, height=250, bg="blue")
        square4 = tk.Canvas(master, width=250, height=250, bg="yellow")
        square5 = tk.Canvas(master, width=250, height=250, bg="white")

        # Create labels for the squares
        label1 = tk.Label(square1, text="Up", bg="red", fg="white", font=("Arial", 20))
        label2 = tk.Label(square2, text="Down", bg="green", fg="white", font=("Arial", 20))
        label3 = tk.Label(square3, text="Left", bg="blue", fg="white", font=("Arial", 20))
        label4 = tk.Label(square4, text="Right", bg="yellow", fg="white", font=("Arial", 20))
        label5 = tk.Label(square5, text="Stop", bg="white", fg="black", font=("Arial", 20))

        # Pack the labels in the center of the squares
        label1.place(relx=0.5, rely=0.5, anchor="center")
        label2.place(relx=0.5, rely=0.5, anchor="center")
        label3.place(relx=0.5, rely=0.5, anchor="center")
        label4.place(relx=0.5, rely=0.5, anchor="center")
        label5.place(relx=0.5, rely=0.5, anchor="center")

        # Pack the squares in the appropriate order
        square1.pack(side="top")
        square2.pack(side="bottom")
        square3.pack(side="left")
        square4.pack(side="right")
        square5.place(relx=0.5, rely=0.5, anchor="center")

# Create the application and run it
root = tk.Tk()
app = App(root)
root.mainloop()

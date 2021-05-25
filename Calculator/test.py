import tkinter as tk

window = tk.Tk()
a = tk.Button(window,text = "abcd")
a.pack()

def y(event):
    print(event.keysym)
a.bind("<Key>",lambda event:y(event))
window.mainloop()
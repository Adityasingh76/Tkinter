import tkinter as tk

window = tk.Tk()
window.wm_attributes("-transparentcolor","#ffffff")
a = tk.Frame(window,bg = "#000000")
a.grid(row = 0,column = 0)
b = tk.Label(a,width = 5,height = 5,bg = "#ffffff")
b.grid(row = 0,column = 0,padx = 30,pady = 30)
window.mainloop()

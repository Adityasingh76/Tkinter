import tkinter as tk
from tkinter.ttk import Combobox


class calculator:
    def __init__(self):
        # creating basic components
        self.window = tk.Tk()
        self.window.title("First Calculator")
        p1 = tk.PhotoImage(file="CalculatorAppList.png")
        self.window.iconphoto(False, p1)
        self.history_box = tk.Frame(master=self.window, height=1)
        self.lab = tk.Label(master=self.history_box, text="History:")
        self.combo = Combobox(master=self.history_box, width=32, state="readonly")
        self.textbox = tk.Entry(master=self.window, width=43)
        self.value = tk.Label(master=self.window, height=1, width=28)
        self.numbers = tk.Frame(master=self.window)
        self.clearing_buttons = tk.Frame(master=self.window)
        self.lst = (1, 2, 3, "+", 4, 5, 6, "-", 7, 8, 9, "*", 0, ".", "=", "/", "BackSpace", "Delete")
        self.str_lst = list(map(str, self.lst))
        self.window.bind("<Key>", self.keyboardbutton)
        self.val, self.indx, self.lst2 = [1, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0], ["+", "-", "*", "/", "=", "C", "B"]
        self.first_value, self.last_button = 0, ""
        self.history, self.w = [], []
        self.combo["values"] = self.history

    def keyboardbutton(self, event):

        if event.keysym == "BackSpace":
            self.insert("B")
        if event.keysym == "Delete":
            self.insert("C")
        if event.keysym == "Return":
            self.insert("=")
        if event.char in self.str_lst:
            print(event.char)
            self.insert(event.char)

    def insert(self, a):
        if str(a).isdigit() or a == ".":
            self.textbox.insert(tk.END, a)
            if self.val[3] == 0:
                self.first_value = self.textbox.get()
            self.val[6] += 1
        else:
            self.indx[2] = self.lst2.index(a)
            if self.indx[2] == 6 and self.last_button != "=":
                if self.last_button == "B":
                    self.last_button = ""
                    h = self.textbox.get()
                    b = self.value.cget("text")
                    if len(h) == 1 and b == "":
                        self.textbox.delete(0, tk.END)
                        h = ""
                        self.val[6] = 0
                        self.val[3] = 0
                    if b == "" and h[:-1] != "":
                        self.textbox.delete(0, tk.END)
                        self.textbox.insert(0, h[:-1])
                        self.val[6] = 0
                        self.val[3] = 0
                    else:
                        if h == "" and b != 0:
                            self.textbox.insert(0, b[:-1])
                            self.value["text"] = ""
                            self.val[6] = 0
                            self.val[3] = 0
                        else:
                            self.textbox.delete(0, tk.END)
                            self.textbox.insert(0, h[:-1])
                            self.val[6] = 0
                            self.val[3] = 0
                else:
                    h = self.textbox.get()[:-1]
                    b = self.value.cget("text")
                    if len(h) == 1:
                        self.textbox.delete(0, tk.END)
                        self.val[6] = 0
                        self.val[3] = 0
                    if b == "" and h != "" and self.textbox.get()[:-1] != "":
                        self.textbox.delete(0, tk.END)
                        self.textbox.insert(0, h)
                        self.val[6] = 0
                        self.val[3] = 0
                    else:
                        if h == "":
                            self.textbox.insert(0, b[:-1])
                            self.value["text"] = ""
                            self.val[6] = 0
                            self.val[3] = 0
                        else:
                            self.textbox.delete(0, tk.END)
                            self.textbox.insert(0, h)
                            self.val[6] = 0
                            self.val[3] = 0
            if self.indx[2] == 1 and self.val[3] == 0:
                self.textbox.insert(tk.END, a)
                self.val[3] = 0
            if self.indx[2] == 5:
                self.value["text"] = ""
                self.first_value = ""
                self.textbox.delete(0, tk.END)
                self.val[3] = 0
                self.val[6] = 0
            if self.indx[2] == 4 and self.val[3] == 0:
                self.val[6] = 0
                self.val[3] = 0
                self.textbox.delete(0, tk.END)
            if self.val[3] == 0 and self.val[6] != 0 and self.indx[2] != 6:
                self.value["text"] = str(self.first_value) + a
            if self.val[6] != 0 or self.last_button == "B":
                self.first_value = self.textbox.get()
                if self.last_button == "B":
                    self.value["text"] = str(self.first_value) + a
                self.textbox.delete(0, tk.END)
                try:
                    self.indx[1] = self.lst2.index(self.value.cget("text")[-1])
                except:
                    pass
                if self.indx[2] == 5:
                    self.value["text"] = ""
                    self.first_value = ""
                    self.textbox.delete(0, tk.END)
                    self.val[3] = -1
                    self.val[6] = 0
                if self.indx[1] == 0 and self.val[3] != 0 and self.indx[2] not in range(4, 6):
                    try:
                        self.history.append(f"{self.value.cget('text')[:-1]} {self.lst2[self.indx[1]]} {self.first_value}")
                        self.first_value = float(self.first_value) + float(self.value.cget("text")[:-1])
                        self.value["text"] = str(float(self.first_value)) + a
                    except:
                        pass

                if self.indx[1] == 1 and self.val[3] != 0 and self.indx[2] not in range(4, 5):
                    try:
                        self.history.append(f"{self.value.cget('text')[:-1]} {self.lst2[self.indx[1]]} {self.first_value}")
                        self.first_value = float(self.value.cget("text")[:-1]) - float(self.first_value)
                        self.value["text"] = str(int(self.first_value)) + a
                    except:
                        pass
                if self.indx[1] == 2 and self.val[3] != 0 and self.indx[2] not in range(4, 5):
                    try:
                        self.history.append(f"{self.value.cget('text')[:-1]} {self.lst2[self.indx[1]]} {self.first_value}")
                        self.first_value = int(self.first_value) * float(self.value.cget("text")[:-1])
                        self.value["text"] = str(self.first_value) + a
                    except:
                        pass
                if self.indx[1] == 3 and self.val[3] != 0 and self.indx[2] not in range(4, 5):
                    try:
                        self.history.append(f"{self.value.cget('text')[:-1]} {self.lst2[self.indx[1]]} {self.first_value}")
                        self.first_value = float(self.value.cget("text")[:-1]) / float(self.first_value)
                        self.value["text"] = str(self.first_value) + a
                    except:
                        pass
                if self.indx[2] == 4 and self.val[3] != 0 and self.indx[1] != 4:
                    if self.indx[1] == 0:
                        self.history.append(f"{self.value.cget('text')[:-1]} {self.lst2[self.indx[1]]} {self.first_value}")
                        self.first_value = float(self.first_value) + float(self.value.cget("text")[:-1])
                        self.value["text"] = str(float(self.first_value))
                    if self.indx[1] == 1:
                        self.history.append(f"{self.value.cget('text')[:-1]} {self.lst2[self.indx[1]]} {self.first_value}")
                        self.first_value = float(self.value.cget("text")[:-1]) - float(self.first_value)
                        self.value["text"] = str(float(self.first_value))
                    if self.indx[1] == 2:
                        self.history.append(f"{self.value.cget('text')[:-1]} {self.lst2[self.indx[1]]} {self.first_value}")
                        self.first_value = float(self.first_value) * float(self.value.cget("text")[:-1])
                        self.value["text"] = str(self.first_value)
                    if self.indx[1] == 3:
                        self.history.append(f"{self.value.cget('text')[:-1]} {self.lst2[self.indx[1]]} {self.first_value}")
                        self.first_value = float(self.value.cget("text")[:-1]) / float(self.first_value)
                        self.value["text"] = str(self.first_value)
                    self.val[3] = -1
                    self.val[6] = 0
                self.val[3] += 1
            else:
                pass
        self.last_button = a
        self.combo["values"] = self.history
        self.combo.current = self.combo["values"][-1]
        print(self.combo["values"],"a")

    def buttons(self):
        val = 0
        p1 = tk.PhotoImage(file="backspace.png").subsample(6, 6)
        self.clear = tk.Button(master=self.numbers, text="C", height=3, width=8,
                               command=lambda x="C": calculator.insert(self, x))
        self.backspace = tk.Button(master=self.numbers, image=p1, height=3, width=8,
                                   command=lambda y="B": calculator.insert(self, y))
        self.backspace.image = p1
        self.clear.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.backspace.grid(row=0, column=2, columnspan=2, sticky="nsew")
        for i in range(1, 5):
            for j in range(4):
                a = self.lst[val]
                self.numbutton = tk.Button(master=self.numbers, text=self.lst[val], height=3, width=8,
                                           command=lambda a=a: calculator.insert(self, a))
                self.numbutton.grid(row=i, column=j, sticky="nsew")
                val += 1

    def packing(self):
        self.lab.pack(side="left")
        self.combo.pack(side="right")
        self.history_box.grid(row=0)
        self.value.grid(row=1)
        self.textbox.grid(row=2, column=0)
        self.clearing_buttons.grid(column=0, row=3)
        self.numbers.grid(column=0, row=4)
        self.window.mainloop()


calc = calculator()
calc.buttons()
calc.packing()


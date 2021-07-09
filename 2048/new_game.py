import random as rd
import tkinter as tk
from tkinter.constants import *

from PIL import Image, ImageTk


class game(tk.Frame):
    def __init__(self, master=None, *args, **kwargs):
        tk.Frame.__init__(self, master=None, *args, **kwargs)
        self.no_of_starting_buttons = 0
        self.movement_no = 0
        self.val,self.val1 = 0,0
        self.val2 = 0
        self.val4 = 0
        self.val5 = 0
        self.val3 = 0
        self.val6 = 0
        self.val8 = 0
        self.button_lst = []
        self.score = 0
        self.highscore = 0
        try:
            self.highscore = open("history.csv","r").readline().split(" ")[-2]
        except:
            pass
        self.undo_button_lst = []
        self.button_image_lst = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.button_lst_right = [[], [], [], []]
        self.button_lst_left = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.button_lst_up = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.button_lst_down = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.p1 = tk.PhotoImage(file="Assets/Blank.png")
        self.p2 = tk.PhotoImage(file="Assets/2.png")
        self.p4 = tk.PhotoImage(file="Assets/4.png")
        self.p8 = tk.PhotoImage(file="Assets/8.png")
        self.p16 = tk.PhotoImage(file="Assets/16.png")
        self.p32 = tk.PhotoImage(file="Assets/32.png")
        self.p64 = tk.PhotoImage(file="Assets/64.png")
        self.p128 = tk.PhotoImage(file="Assets/128.png")
        self.p256 = tk.PhotoImage(file="Assets/256.png")
        self.p512 = tk.PhotoImage(file="Assets/512.png")
        self.p1024 = tk.PhotoImage(file="Assets/1024.png")
        self.p2048 = tk.PhotoImage(file="Assets/2048.png")
        self.button_dict = ["pyimage1","pyimage2","pyimage3","pyimage4","pyimage5","pyimage6","pyimage7","pyimage8","pyimage9","pyimage10","pyimage11","pyimage12"]
        self.button_no = [self.p1,self.p2,self.p4,self.p8,self.p16,self.p32,self.p64,self.p128,self.p256,self.p512,self.p1024,self.p2048]
        self.score_lst = [0,2,4,8,16,32,64,128,256,512,1024,2048]
        self.pclose = ImageTk.PhotoImage(Image.open("Assets/Close.png").resize((27, 24), Image.ANTIALIAS))
        self.pminimize = ImageTk.PhotoImage(Image.open("Assets/minimize.png").resize((27, 9), Image.ANTIALIAS))
        self.pmain_photo = ImageTk.PhotoImage(Image.open("Assets/main.png").resize((150, 150), Image.ANTIALIAS))
        self.poptions = ImageTk.PhotoImage(Image.open("Assets/Options.png").resize((32,29),Image.ANTIALIAS))
        self.pscore = ImageTk.PhotoImage(Image.open("Assets/Score.png").resize((110,70),Image.ANTIALIAS))
        self.pnewgame = ImageTk.PhotoImage(file = "Assets/newgame.png")





    def create_basics(self):
     #--------------------------------------------------
        self.options_frame = tk.Frame(self,bg = "#cdb990")
        self.options_button = tk.Button(self.options_frame,image = self.poptions,bg = "#cdb990",borderwidth = 0)
        self.options_button.pack(anchor = E,padx = 10,pady = 10)
        self.options_button.bind("<Button-1>",lambda event: self.main_menu(event))
        self.options_frame.pack(fill = X)
        # -------------------------------------------------------------------------------------------------
        self.center = tk.Frame(self, bg="#cdb990")
        self.center.pack(fill=X)
        # -------------------------------------------------
        self.score_highscore_frame = tk.Frame(self.center,bg = "#cdb990")
        self.score_highscore_frame.grid(row = 0,column = 2,sticky = N,pady = 29)
        #--------------------------------------------------
        self.score_frame = tk.Frame(self.score_highscore_frame, bg="#a9815b")
        self.score_text = tk.Label(self.score_frame, width=14, height=1, bg="#a9815b", fg="#ffffff", text="Score",
                                   font=("Arial", 10, "bold"), anchor="n")
        self.score_text.pack(side=TOP)
        self.score_number = tk.Label(self.score_frame, height=1, bg="#a9815b", fg="#ffffff", text="0",
                                     font=("Arial", 20, "bold"))
        self.score_number.pack(side=BOTTOM,pady = 5)
        self.score_frame.grid(row = 0,column = 0,padx = 10,sticky = N)
        #--------------------------------------------------
        self.test_frame = tk.Frame(self.center,width = 100,bg = "#cdb990")
        self.test_frame.grid(row = 0,column = 1)
        # -------------------------------------------------
        self.high_score_frame = tk.Frame(self.score_highscore_frame, bg="#a9815b")
        self.high_score_text = tk.Label(self.high_score_frame, height=1, bg="#a9815b", fg="#ffffff",
                                        text="High Score",
                                        font=("Arial", 10, "bold"), anchor="n")
        self.high_score_text.pack(side=TOP, pady=5)
        self.high_score_number = tk.Label(self.high_score_frame, width=7, height=1, bg="#a9815b", fg="#ffffff",
                                          text=self.highscore,
                                          font=("Arial", 20, "bold"))
        self.high_score_number.pack(side=BOTTOM)
        self.high_score_frame.grid(row = 0,column = 1,padx = 10,sticky = N)
        # ---------------------------------------------------
        self.undo_reset = tk.Frame(self.score_highscore_frame,bg= "#cdb990")
        self.undo_reset.grid(row = 1,columnspan = 2,column = 0,sticky = E)
        self.undo_button = tk.Button(self.undo_reset,text = "Undo" , bg = "#a9815b",fg = "#ffffff",font = ("Arial",15,"bold"),borderwidth = 0)
        self.undo_button.grid(row = 1,column = 0,padx = 10,pady=10)
        self.undo_button.bind("<Button-1>",lambda event:self.undo(event))
        self.reset_button = tk.Button(self.undo_reset,bg = "#a9815b",fg = "#ffffff",text = "Reset",font = ("Arial",15,"bold"),borderwidth = 0)
        self.reset_button.grid(row = 1,column = 1,padx = 10,pady = 10)
        self.reset_button.bind("<Button-1>",lambda event:self.reset_game(event))
        self.main_photo = tk.Label(self.center, image=self.pmain_photo)
        self.main_photo.grid(row = 0,column = 0,padx = 10,pady = 10)
        # --------------------------------------------------------------------------------------------------
        self.main1 = tk.Frame(self,bg = "#c99966")
        self.main1.pack(padx = 10,pady = 10)
        self.main = tk.Frame(self.main1,bg = "#c99966")
        self.main.pack(padx = 10,pady = 34)
    def reset_game(self,event):
        self.main.pack_forget()

        self.main = tk.Frame(self.main1, bg="#c99966")
        self.main.pack(padx=10, pady=34)
        self.score = 0
        self.score_number["text"] = "0"
        self.button_lst = []
        self.undo_button_lst = []
        self.button_image_lst = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.button_lst_right = [[], [], [], []]
        self.button_lst_left = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.button_lst_up = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.button_lst_down = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.create_buttons()
    def bind_keyboard_buttons(self):
        global menu1
        self.master.bind("<Up>", lambda event,x = "Up": self.move_buttons(event, x, 4))
        self.master.bind("<Down>", lambda event , x = "Down": self.move_buttons(event, x, 4))
        self.master.bind("<Right>", lambda event,x = "Right": self.move_buttons(event, x, 4))
        self.master.bind("<Left>", lambda event,x = "Left": self.move_buttons(event, x, 4))
        self.bind("<Button-1>",lambda event:self.delete_menu(event))
    def delete_menu(self,event):
        global menu1
        try:
            menu1.grid_forget()
        except:
            pass

    def move_buttons(self,event,x,z):
        self.val2 = 0
        self.movement_no = 0
        self.undo_button_lst = self.button_lst
        for i in range(z):
            for j in range(z):
                try:
                    self.button_image_lst[i][j] = self.button_no[self.button_dict.index(self.button_lst[i][j]["image"])]
                except:
                    pass
        self.merge_buttons(x, z)

        if self.val2 == z:
            self.check_result()

        self.score_number["text"] = str(self.score)
        if int(self.high_score_number["text"]) <= self.score:
            self.high_score_number["text"] = self.score
        new_button = []
        for a in range(z):
            for b in range(z):
                if self.button_lst[a][b]["image"] == "pyimage1":
                    new_button.append(self.button_lst[a][b])
        try:
            new_button[0]["image"] = new_button[0]["image"]
            if self.movement_no != 0:
                rd.choice(new_button)["image"] = rd.choice([self.p2, self.p4])
        except IndexError:
            self.check_result()
        self.history = open("history.csv", "w")
        for c in range(z):
            for d in range(z):
                self.history.writelines(self.button_lst[c][d]["image"] + " ")
                if self.button_lst[c][d]["image"] == "pyimage12":
                    self.val5 = 1
        self.history.writelines(str(self.score) + " ")
        self.history.writelines(str(self.high_score_number["text"]) + " ")
        if self.button_lst == self.button_lst_right:
            self.history.writelines("Right")
        if self.button_lst == self.button_lst_left:
            self.history.writelines("Left")
        if self.button_lst == self.button_lst_up:
            self.history.writelines("Up")
        if self.button_lst == self.button_lst_down:
            self.history.writelines("Down")

        self.history.close
        if self.val6 == 0:
            self.undo_button_lst = self.button_lst
        self.val6 += 1
        if self.val5 == 1:
            self.end_game(event)
    def check_result(self):
        directions = ["Right","Left","Up","Down"]
        a = 0
        for i in range(4):
            self.merge_buttons(directions[i], 4)
            a += self.movement_no
        if a != 0:
            pass
        else:
            b = tk.Label(self.master, width=10, height=1, bg="#a39489", fg="#ffcc00", text="Game Over",
                         font=("Helvetica", 58, "bold"))
            b.grid(row=0, column=0)
    def merge_buttons(self,x,z):
        self.val2 = 0
        self.val8 = 0
        self.movement_no = 0
        if x == "Right":
            self.button_lst = self.button_lst_right
        if x == "Left":
            self.button_lst = self.button_lst_left
        if x == "Up":
            self.button_lst = self.button_lst_up
        if x == "Down":
            self.button_lst = self.button_lst_down
        for k in range(z):
            for i in range(z):
                for j in range(1,z):
                    if self.button_lst[i][z-j]["image"] == "pyimage1":
                        if self.button_lst[i][z-j-1]["image"] != "pyimage1":
                            self.button_lst[i][z-j]["image"] = self.button_lst[i][z-j-1]["image"]
                            self.button_lst[i][z-j-1]["image"] = self.p1
                            self.movement_no += 1
        x = 0
        print(1)
        for i in range(z):
            x = 0
            for k in range(z):
                self.val8 = 0
                for j in range(x+1, z):
                    if self.button_lst[i][z - j]["image"] == "pyimage1":
                        if self.button_lst[i][z - j - 1]["image"] != "pyimage1":
                            self.button_lst[i][z - j]["image"] = self.button_lst[i][z - j - 1]["image"]
                            self.button_lst[i][z - j - 1]["image"] = self.p1
                            self.movement_no += 1
                            continue
                    if self.button_lst[i][z - j]["image"] == self.button_lst[i][z - j - 1]["image"] and self.button_lst[i][z-j]["image"] != "pyimage1":
                        self.button_lst[i][z - j]["image"] = self.button_no[self.button_dict.index(self.button_lst[i][z - j - 1]["image"])+1]
                        self.score += self.score_lst[self.button_dict.index(self.button_lst[i][z-j-1]["image"]) + 1]
                        self.button_lst[i][z - j - 1]["image"] = self.p1
                        self.movement_no += 1
                    if j == 1 and self.button_lst[i][z - j]["image"] != "pyimage1" and self.button_lst[i][z - j - 1]["image"] != "pyimage1" and self.button_lst[i][z - j]["image"] != self.button_lst[i][z - j - 1]["image"]:
                        self.val8 += 1
                    print(f"j:{j}")
                print(f"k:{k}")
                x += 1
            if self.val8 == z-1:
                self.val2 += 1
                self.movement_no = 0

            print(f"i:{i}")

    def minimize_window(self, event):
        self.master.overrideredirect(0)
        self.master.wm_state("iconic")
    def main_menu(self,event):
        self.create_menu = menu(self.master)
        self.create_menu.grid(row = 0,column = 0)
    def end_game(self,event):
        a = tk.Label(self.master,width = 10,height = 1,bg = "#a39489",fg = "#ffcc00",text = "You Won",font = ("Helvetica",58,"bold"))
        a.grid(row= 0,column = 0)
    def undo(self,event):
        for x in range(4):
            for y in range(4):
                try:
                    self.undo_button_lst[x][y]["image"] = self.button_image_lst[x][y]
                except:
                    pass

    def create_buttons(self):
        self.no_of_starting_buttons = 0
        for i in range(4):
            for j in range(4):
                self.button = tk.Label(self.main, image=self.p1,bg = "#c99966")
                self.button.image = self.p1
                self.button.grid(row=i, column=j)
                self.button_lst_right[i].append(self.button)
                self.button_lst_left[i][3-j] = self.button
                self.button_lst_up[j][3-i] = self.button
                self.button_lst_down[j][i] = self.button
                if rd.randint(0, 9) % 3 == 0 and self.no_of_starting_buttons <= 1:
                    if self.no_of_starting_buttons == 0:
                        self.button["image"] = self.p2
                        self.button.image = self.p2
                    else:
                        self.button["image"] = self.p4
                        self.button.image = self.p4
                    self.no_of_starting_buttons += 1


class menu(tk.Frame):
    def __init__(self,master=None,*args,**kwargs):
        tk.Frame.__init__(self,master = None,*args,**kwargs)
        self.resume_game_button = tk.Button(self, width=16, height=1, bg="#ff0000", fg="#ffffff", text="Resume",
                                            font=("Arial", 20, "bold"), borderwidth=0.5)
        self.resume_game_button.pack(side=TOP, pady = (30, 0))
        self.resume_game_button.bind("<Button-1>",lambda event:self.resume_game(event))
        self.new_game_button = tk.Button(self, width=16, height=1, bg="#ff0000", fg="#ffffff", text="New Game",
                                         font=("Arial", 20, "bold"), borderwidth=0.5)
        self.new_game_button.bind("<Button-1>", lambda event: self.new_game(event))
        self.new_game_button.pack(side=TOP, pady=(30, 0))
        self.exit_button = tk.Button(self,width = 16,height = 1,bg = "#ff0000",fg="#ffffff",text = "Exit",font = ("Arial",20,"bold"),borderwidth = 0.5)
        self.exit_button.pack(side = BOTTOM,pady = 30,padx = 10)
        self.exit_button.bind("<Button-1>",lambda event:self.master.destroy())


    def new_game(self,event):
        global ex
        ex.reset_game(event)
        self.grid_forget()
    def resume_game(self,event):
        global ex
        ex.reset_game(event)
        a = open("history.csv","r")
        lst = a.readline().split(" ")
        w = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
        if lst[-1] == "Down":
            for a in range(4):
                for b in range(4):
                    ex.button_lst_down[a][b]["image"] = ex.button_no[ex.button_dict.index(lst[w[a][b]])]
        if lst[-1] == "Up":
            for a in range(4):
                for b in range(4):
                    ex.button_lst_up[a][b]["image"] = ex.button_no[ex.button_dict.index(lst[w[a][b]])]
        if lst[-1] == "Left":
            for a in range(4):
                for b in range(4):
                    ex.button_lst_left[a][b]["image"] = ex.button_no[ex.button_dict.index(lst[w[a][b]])]
        if lst[-1] == "Right":
            for a in range(4):
                for b in range(4):
                    ex.button_lst_right[a][b]["image"] = ex.button_no[ex.button_dict.index(lst[w[a][b]])]
        try:
            ex.score_number["text"] = lst[-3]
            ex.high_score_number["text"] = lst[-2]
        except:
            pass
        self.grid_forget()



if __name__ == "__main__":
    window = tk.Tk()
    menu1 = menu(window)
    ex = game(window, height=750, width=750,bg = "#cdb990")
    ex.create_basics()
    ex.bind_keyboard_buttons()
    ex.create_buttons()
    ex.grid(row = 0,column = 0)
    menu1 = menu(window)
    menu1.grid(row=0, column=0)
    window.mainloop()

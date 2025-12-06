from customtkinter import *
from random import *


class Wordle(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("430x450")
        self.title("Wordle")
        self.words = ["земля", "місто", "серце", "книга", "зерно", "кішка", "річка","свято","горіх","зірка",
                      "тепло","голод","весна","пісня","сонце","листя","цукор","щастя","вітер","вечір","вітка"]

        self.ans = choice(self.words)
        self.input_ = CTkEntry(self, width=250, height=40)
        self.enter_word = CTkButton(self, text="OK", width=80, height=40, command=self.check_word)
        self.input_.place(x=90, y=380)
        self.enter_word.place(x=350, y=380)

        self.adaptive_interface()
        self.boxes = []
        x = 20
        for i in range(5):
            box = CTkLabel(self, width=70, height=70, text="", fg_color="gray20", corner_radius=10, font=("Arial", 28))
            box.place(x=x, y=30)
            self.boxes.append(box)
            x += 75
            self.right_boxes = []
        x = 20
        for i in range(5):
            box = CTkLabel(self, width=70, height=70, text="", fg_color="gray20", corner_radius=10,
                           font=("Arial", 28))
            box.place(x=x, y=120)
            self.right_boxes.append(box)
            x += 75

    def check_word(self):
        word = self.input_.get().lower()
        if len(word) != 5:
            print("Введи 5-буквенне слово!")
            return
        for i in range(5):
            letter = word[i]
            self.boxes[i].configure(text=letter.upper())
            if letter == self.ans[i]:
                self.boxes[i].configure(fg_color="green")
                self.right_boxes[i].configure(fg_color="green")
                self.right_boxes[i].configure(text=letter.upper())
            elif letter in self.ans:
                self.boxes[i].configure(fg_color="gold")
            else:
                self.boxes[i].configure(fg_color="gray40")
    def adaptive_interface(self):
        self.enter_word.place(x=self.winfo_width()-90, y=self.winfo_height()-70)
        self.input_.place(x=self.winfo_width()-350, y=self.winfo_height()-70)

        self.after(50, self.adaptive_interface)

window = Wordle()
window.mainloop()
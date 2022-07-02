from tkinter import *

class Paint(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.setUI()

    def setUI(self):
        self.parent.title("Painter")
        self.pack(fill=BOTH, expand=1)

        self.columnconfigure(6, weight=1)
        self.rowconfigure(2, weight=1)

        self.canv = Canvas(self, bg="white")
        self.canv.grid(row=2, column=0, columnspan=7,
                       padx=5, pady=5, sticky=E + W + S + N)

        color_lab = Label(self, text="Color: ")
        color_lab.grid(row=0, column=0, padx=6)

        red_btn = Button(self, text='Red', width=10)
        red_btn.grid(row=0, column=1)

        green_btn = Button(self, text='Green', width=10)
        green_btn.grid(row=0, column=2)

        blue_btn = Button(self, text='Blue', width=10)
        blue_btn.grid(row=0, column=3)

        black_btn = Button(self, text='Black', width=10)
        black_btn.grid(row=0, column=4)

        white_btn = Button(self, text='White', width=10)
        white_btn.grid(row=0, column=5)

        size_lab = Label(self, text='Brush size: ')
        size_lab.grid(row=1, column=0, padx=5)
        one_btn = Button(self, text='Two', width=10)
        one_btn.grid(row=1, column=1)

        two_btn = Button(self, text='Five', width=10)
        two_btn.grid(row=1, column=2)

        three_btn = Button(self, text='Seven', width=10)
        three_btn.grid(row=1, column=3)

        four_btn = Button(self, text='Ten', width=10)
        four_btn.grid(row=1, column=4)

        five_btn = Button(self, text='Twenty', width=10)
        five_btn.grid(row=1, column=5)

        six_btn = Button(self, text='Fifty', width=10)
        six_btn.grid(row=1, column=6)




def main():
    root = Tk()
    root.geometry("1280x800+300+300")
    app = Paint(root)
    root.mainloop()


if __name__ == "__main__":
    main()
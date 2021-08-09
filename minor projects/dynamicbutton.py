from tkinter import *

class SampleApp(Tk):

    def __init__(self, s):

        Tk.__init__(self)
        self.title("GUI")
        x = 200
        y = s*30
        self.geometry(str(x) + "x" + str(y))

        for i in range(1, s+1):

            self.button = Label(self, text="Button " + str(i))
            self.button.pack()

app = SampleApp(7)
app.mainloop()
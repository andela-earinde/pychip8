#!/usr/bin/python

import Tkinter


class Renderer(Tkinter.Frame):

    def __init__(self, master=None):
        Tkinter.Frame.__init__(self, master)
        self.pack()
        self.create_widgets()

    def say_hi(self):
        print "hi there, everyone!"

    def create_widgets(self):
        self.QUIT = Tkinter.Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Tkinter.Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})

root = Tkinter.Tk()
app = Renderer(master=root)
app.mainloop()
root.destroy()

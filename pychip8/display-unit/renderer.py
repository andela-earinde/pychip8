#!/usr/bin/python

import Tkinter


class Renderer(Tkinter.Frame):

    def __init__(self, master=None):
        Tkinter.Frame.__init__(self, master)
        self.pack()
        self.canvas = Tkinter.Canvas(master, width=640, height=320)
        self.canvas.pack()
        self.screen = self.canvas.create_rectangle(
            0, 0, 640, 320, fill="black")

    def clear_display(self):
        self.canvas.delete(self.screen)
        self.screen = self.canvas.create_rectangle(
            0, 0, 640, 320, fill="black")

    def draw_graphics(self, display):
        self.clear_display()
        for i, j in enumerate(display):
            x_cord = (i % 64) * 10
            y_cord = (i / 64) * 10


root = Tkinter.Tk()
app = Renderer(master=root)
app.mainloop()
root.destroy()

#!/usr/bin/python

import Tkinter


class Renderer(Tkinter.Frame):

    def __init__(self, master=Tkinter.Tk()):
        self.master = master
        Tkinter.Frame.__init__(self, self.master)
        self.pack()
        self.canvas = Tkinter.Canvas(self.master, width=640, height=320)
        self.canvas.pack()
        self.screen = self.canvas.create_rectangle(
            0, 0, 640, 320, fill="black")

    def clear_display(self):
        self.canvas.delete(self.screen)
        self.screen = self.canvas.create_rectangle(
            0, 0, 640, 320, fill="black")

    def draw_graphics(self, display):
        import pdb; pdb.set_trace()
        self.clear_display()
        for i, j in enumerate(display):
            x_cord = (i % 64) * 10
            y_cord = (i / 64) * 10

            if display[i]:
                self.canvas.create_rectangle(
                    x_cord, y_cord, 10, 10, fill="white")
            else:
                self.canvas.create_rectangle(
                    x_cord, y_cord, 10, 10, fill="black")

            self.master.update_idletasks()

    def initialize_screen(self):
        self.master.update()

app = Renderer()

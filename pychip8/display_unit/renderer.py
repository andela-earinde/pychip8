#!/usr/bin/python
import pyglet
import os


class Renderer(pyglet.window.Window):

    def __init__(self):
        self.pixel = pyglet.image.load(
            'pixel.png',
            file=open('%s/pychip8/pixel.png' % (os.getcwd()), 'rb')
        )

    def on_key_press(self, symbol, modifiers):
        pass

    def on_key_release(self, symbol, modifiers):
        pass

    def draw_graphics(self, display):
        self.clear()
        for i in xrange(0, len(display)):
            x_cord = (i % 64) * 10
            y_cord = (i / 64) * 10
            if display[i]:
                self.pixel.blit(x_cord, 310 - y_cord)
        self.flip()

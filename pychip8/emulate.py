"""
The main process
"""
import os
from functools import partial

from cpu.cpu import Chip8
from display_unit.renderer import Renderer

chip8 = Chip8()
chip8.initialize()

loaded_program = []

with open('%s/pychip8/roms/MISSILE' % (os.getcwd()), 'r') as file:
    for byte in iter(partial(file.read, 1), b''):
        loaded_program.append(ord(byte))

chip8.load_program(loaded_program)

renderer = Renderer(640, 320)

chip8.set_renderer(renderer)

renderer.dispatch_events()

chip8.emulate_cpu()

"""
This module contains the class to handle the opcode execution

This variables are used in the comments:
nnn or addr - A 12-bit value, the lowest 12 bits of the instruction
n or nibble - A 4-bit value, the lowest 4 bits of the instruction
x - A 4-bit value, the lower 4 bits of the high byte of the instruction
y - A 4-bit value, the upper 4 bits of the low byte of the instruction
kk or byte - An 8-bit value, the lowest 8 bits of the instruction
"""

from random import randint

from pychip8.cpu.eight_subcases import eight_subcases
from pychip8.cpu.e_subcases import e_subcases
from pychip8.cpu.f_subcases import f_subcases


class OpcodeExecutor(object):

    def __init__(self, cpu):
        # the cpu instance passed
        self.cpu = cpu

    def _clear_display(self):
        """
        Clear the display.
        """
        self.cpu.renderer.clear_display()
        for i, j in enumerate(self.cpu.display):
            self.cpu.display[i] = 0

    def _return_from_subroutine(self):
        """
        Return from a subroutine.
        The interpreter sets the program counter to the address at the top
        of the stack, then subtracts 1 from the stack pointer.
        """
        self.cpu.pc = self.cpu.stack.pop()
        self.cpu.stack_pointer -= 1

    def _execute_zero(self, opcode):
        """
        Execute the zero opcode subcases
        """
        zero_subcases = {
            0x00E0: self._clear_display,
            0x00EE: self._return_from_subroutine
        }
        zero_subcases[opcode]()

    def _execute_one(self, opcode):
        """
        Jump to location nnn.
        The interpreter sets the program counter to nnn.
        """
        self.cpu.pc = opcode & 0x0fff

    def _execute_two(self, opcode):
        """
        Call subroutine at nnn.
        The interpreter increments the stack pointer, then puts the
        current PC on the top of the stack. The PC is then set to nnn.
        """
        self.cpu.stack_pointer += 1
        self.cpu.stack.append(self.cpu.pc)
        self.cpu.pc = opcode & 0x0fff

    def _execute_three(self, opcode):
        """
        Skip next instruction if Vx = kk.
        The interpreter compares register Vx to kk, and if they are equal,
        increments the program counter by 2.
        """
        if self.cpu.Vx[self.x] == (opcode & 0x00ff):
            self.cpu.pc += 2

    def _execute_four(self, opcode):
        """
        Skip next instruction if Vx != kk.
        The interpreter compares register Vx to kk, and if they are not equal,
        increments the program counter by 2.
        """
        if self.cpu.Vx[self.x] != (opcode & 0x00ff):
            self.cpu.pc += 2

    def _execute_five(self, opcode):
        """
        Skip next instruction if Vx = Vy.
        The interpreter compares register Vx to register Vy, and if
        they are equal, increments the program counter by 2.
        """
        if self.cpu.Vx[self.x] == self.cpu.Vx[self.y]:
            self.cpu.pc += 2

    def _execute_six(self, opcode):
        """
        Set Vx = kk.
        The interpreter puts the value kk into register Vx.
        """
        self.cpu.Vx[self.x] = opcode & 0x00ff

    def _execute_seven(self, opcode):
        """
        Set Vx = Vx + kk.
        Adds the value kk to the value of register Vx,
        then stores the result in Vx.
        """
        self.cpu.Vx[self.x] += opcode & 0x00ff

    def _execute_eight(self, opcode):
        """
        Execute for primary opcodes that begin with eight
        """
        eight_subcases[opcode & 0x000f](self.cpu, self.x, self.y)

    def _execute_a(self, opcode):
        """
        Set I = nnn.
        The value of register I is set to nnn.
        """
        self.cpu.I = opcode & 0x0fff

    def _execute_b(self, opcode):
        """
        Jump to location nnn + V0.
        The program counter is set to nnn plus the value of V0.
        """
        self.cpu.pc = (opcode & 0x0fff) + self.cpu.Vx[0]

    def _execute_c(self, opcode):
        """
        Set Vx = random byte AND kk.
        The interpreter generates a random number from 0 to 255,
        which is then ANDed with the value kk. The results are
        stored in Vx. See instruction 8xy2 for more information on AND.
        """
        self.cpu.Vx[self.x] = randint(0, 0xff) & (opcode & 0x00ff)

    def _execute_d(self, opcode):
        """
        Display n-byte sprite starting at memory location I at (Vx, Vy),
        set VF = collision. The interpreter reads n bytes from memory,
        starting at the address stored in I. These bytes are then displayed
        as sprites on screen at coordinates (Vx, Vy). Sprites are XORed onto
        the existing screen. If this causes any pixels to be erased,
        VF is set to 1, otherwise it is set to 0. If the sprite is positioned
        so part of it is outside the coordinates of the display, it wraps
        around to the opposite side of the screen.
        """
        self.cpu.Vx[0xf] = 0
        xcord = self.cpu.Vx[self.x]
        ycord = self.cpu.Vx[self.y]
        height = opcode & 0x000f
        pixel = 0

        for i in xrange(0, height):
            pixel = self.cpu.memory[self.cpu.I + i]
            for j in xrange(0, 8):
                dx = xcord + j
                dy = ycord + i
                if (pixel & (0x80 >> j)) != 0:
                    if self.cpu.display[dx + (dy * self.cpu.display_width)]:
                        self.cpu.Vx[0xf] = 1
                    self.cpu.set_display(dx, dy)
            self.cpu.drawFlag = True

    def _execute_e(self, opcode):
        e_subcases[opcode & 0x00ff](self.cpu, self.x)

    def _execute_f(self, opcode):
        f_subcases[opcode & 0x00ff](self.cpu, self.x)

    def execute(self, opcode, x, y):
        """
        The main opcodes for execution
        """
        main_cases = {
            0x0000: self._execute_zero,
            0x1000: self._execute_one,
            0x2000: self._execute_two,
            0x3000: self._execute_three,
            0x4000: self._execute_four,
            0x5000: self._execute_five,
            0x6000: self._execute_six,
            0x7000: self._execute_seven,
            0x8000: self._execute_eight,
            0xA000: self._execute_a,
            0xB000: self._execute_b,
            0xC000: self._execute_c,
            0xD000: self._execute_d,
            0xE000: self._execute_e,
            0xF000: self._execute_f
        }
        self.x = x
        self.y = y
        main_cases[opcode & 0xf000](opcode)

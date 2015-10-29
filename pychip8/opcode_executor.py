"""
This module contains the class to handle the opcode execution

This variables are used in the comments:
nnn or addr - A 12-bit value, the lowest 12 bits of the instruction
n or nibble - A 4-bit value, the lowest 4 bits of the instruction
x - A 4-bit value, the lower 4 bits of the high byte of the instruction
y - A 4-bit value, the upper 4 bits of the low byte of the instruction
kk or byte - An 8-bit value, the lowest 8 bits of the instruction
"""


class OpcodeExecutor(object):

    def __init__(self, cpu, x, y):
        # the cpu instance passed
        self.cpu = cpu
        self.x = x
        self.y = y

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
        self.cpu.stackPointer -= 1

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
        self.cpu.stackPointer += 1
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
        eight_subcases = {
            0x0000: _zero_eight_execution,
            0x0001: _first_eight_execution,
            0x0002: _second_eight_execution,
            0x0003: _third_eight_execution,
            0x0004: _fourth_eight_execution,
            0x0005: _fifth_eight_execution,
            0x0006: _sixth_eight_execution,
            0x0007: _seventh_eight_execution,
            0x000E: _eight_eight_execution
        }

    def execute(self, opcode):
        pass

    """
    Primary opcodes for the main execution
    """
    MAIN_CASES = {
        0x0000: _execute_zero,
        0x1000: _execute_one,
        0x2000: _execute_two,
        0x3000: _execute_three,
        0x4000: _execute_four,
        0x5000: _execute_five,
        0x6000: _execute_six,
        0x7000: _execute_seven,
        0x8000: _execute_eight,
        0xA000: _execute_A,
        0xB000: _execute_B,
        0xC000: _execute_C,
        0xD000: _execute_D,
        0xE000: _execute_E,
        0xF000: _execute_F
    }


    """
    Subopcodes for primary opcodes that begin with f
    """
    F_SUBCASES = {
        0x0007: _first_f_execution,
        0x000A: _second_f_execution,
        0x0015: _third_f_execution,
        0x0018: _fourth_f_execution,
        0x001E: _fifth_f_execution,
        0x0029: _sixth_f_execution,
        0x0033: _seventh_f_execution,
        0x0055: _eight_f_execution,
        0x0065: _ninth_f_execution
    }
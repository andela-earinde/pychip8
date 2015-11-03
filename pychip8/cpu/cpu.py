"""
 This module will contain the cpu for executing the chip8 opcodes and all
 other cpu related operations. It is a large class on purpose to gather all
 thoughts into a single place and make reading the program easier
"""

from pychip8.opcode_executor import OpcodeExecutor


class Chip8(object):

    def __init__(self):
        # program counter
        self.pc = 0

        # register used to store memory address, 16-bit
        self.I = None

        # Initialize the Arithmetic logic unit
        self.opcode_executor = OpcodeExecutor(self)

        # 8-bit storage
        self.soundTimer = None

        self.isRunning = False

        # 8-bit storage
        self.delayTimer = None

        # 8-bit storage
        self.stackPointer = None

        # set of hex characters for representing
        # some characters
        self.hexChars = [
            0xF0, 0x90, 0x90, 0x90, 0xF0,  # 0
            0x20, 0x60, 0x20, 0x20, 0x70,  # 1
            0xF0, 0x10, 0xF0, 0x80, 0xF0,  # 2
            0xF0, 0x10, 0xF0, 0x10, 0xF0,  # 3
            0x90, 0x90, 0xF0, 0x10, 0x10,  # 4
            0xF0, 0x80, 0xF0, 0x10, 0xF0,  # 5
            0xF0, 0x80, 0xF0, 0x90, 0xF0,  # 6
            0xF0, 0x10, 0x20, 0x40, 0x40,  # 7
            0xF0, 0x90, 0xF0, 0x90, 0xF0,  # 8
            0xF0, 0x90, 0xF0, 0x10, 0xF0,  # 9
            0xF0, 0x90, 0xF0, 0x90, 0x90,  # A
            0xE0, 0x90, 0xE0, 0x90, 0xE0,  # B
            0xF0, 0x80, 0x80, 0x80, 0xF0,  # C
            0xE0, 0x90, 0x90, 0x90, 0xE0,  # D
            0xF0, 0x80, 0xF0, 0x80, 0xF0,  # E
            0xF0, 0x80, 0xF0, 0x80, 0x80   # F
        ]

    def initialize(self):
        self.pc = 0x200

        self.step = 0

        self.I = 0

        self.keys = []

        self.soundTimer = 0

        self.memory = []

        self.delayTimer = 0

        self.stackPointer = 0

        self.displayWidth = 64

        self.displayHeight = 32

        self.drawFlag = False

        self.display = []

        # registers 8-bit
        self.Vx = []

        # 16-bit long stack
        self.stack = []

        for i, chars in enumerate(self.hexChars):
            self.memory[i] = chars

    def load_program(self, program):
        for i, chars in enumerate(program):
            self.memory[0x200 + i] = chars

    def clear_screen(self):
        self.renderer.clear_display()
        for i, j in enumerate(self.display):
            self.display[i] = 0

    def start_cycle(self):
        opcode = self.memory[self.pc] << 8 | self.memory[self.pc + 1]
        x = (opcode & 0x0f00) >> 8
        y = (opcode & 0x00f0) >> 4

        self.pc += 2

        self.opcode_executor.execute(opcode, x, y)

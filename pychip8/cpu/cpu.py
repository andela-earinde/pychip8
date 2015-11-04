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
        self.sound_timer = None

        self.is_running = False

        # 8-bit storage
        self.delay_timer = None

        # 8-bit storage
        self.stack_pointer = None

        # set of hex characters for representing
        # some characters
        self.hex_chars = [
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

        self.sound_timer = 0

        self.memory = []

        self.delay_timer = 0

        self.stack_pointer = 0

        self.display_width = 64

        self.display_height = 32

        self.draw_flag = False

        self.display = []

        # registers 8-bit
        self.Vx = []

        # 16-bit long stack
        self.stack = []

        for i, chars in enumerate(self.hexChars):
            self.memory[i] = chars

    def load_program(self, program):
        """
        Load the program into memory
        """
        for i, chars in enumerate(program):
            self.memory[0x200 + i] = chars

    def clear_screen(self):
        """
        clear the display
        """
        self.renderer.clear_display()
        for i, j in enumerate(self.display):
            self.display[i] = 0

    def set_display(self, dx, dy):
        """
        Handle the logic for setting the display
        """
        if dx > self.display_width:
            dx -= self.display_width
        elif dx < 0:
            dx += self.display_width

        if dx > self.display_height:
            dx -= self.display_width
        elif dx < 0:
            dx += self.display_height

        self.display[dx + (dy * self.display_width)] ^= 1

    def start_cycle(self):
        """
        Start the cpu execution cycle, this is the point where
        the opcodes are analyzed
        """
        opcode = self.memory[self.pc] << 8 | self.memory[self.pc + 1]
        x = (opcode & 0x0f00) >> 8
        y = (opcode & 0x00f0) >> 4

        self.pc += 2

        self.opcode_executor.execute(opcode, x, y)

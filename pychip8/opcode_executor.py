"""
This module contains the class to handle the opcode execution
"""


class OpcodeExecutor(object):

    MAIN_CASES = {
        0x0000: execute_zero,
        0x1000: execute_one,
        0x2000: execute_two,
        0x3000: execute_three,
        0x4000: execute_four,
        0x5000: execute_five,
        0x6000: execute_six,
        0x7000: execute_seven,
        0x8000: execute_eight,
        0xA000: execute_A,
        0xB000: execute_B,
        0xC000: execute_C,
        0xD000: execute_D,
        0xE000: execute_E,
        0xF000: execute_F
    }

    ZERO_SUBCASES = {
        0x00E0: clear_display,
        0xEE: return_from_subroutine
    }

    EIGHT_SUBCASES = {
        0x0000: zero_eight_execution,
        0x0001: first_eight_execution,
        0x0002: second_eight_execution,
        0x0003: third_eight_execution,
        0x0004: fourth_eight_execution,
        0x0005: fifth_eight_execution,
        0x0006: sixth_eight_execution,
        0x0007: seventh_eight_execution,
        0x000E: eight_eight_execution
    }

    F_SUBCASES = {
        0x0007: first_f_execution,
        0x000A: second_f_execution,
        0x0015: third_f_execution,
        0x0018: fourth_f_execution,
        0x001E: fifth_f_execution,
        0x0029: sixth_f_execution,
        0x0033: seventh_f_execution,
        0x0055: eight_f_execution,
        0x0065: ninth_f_execution
    }

    def __init__(self, cpu, x, y):
        # the cpu instance passed
        self.cpu = cpu
        self.Vx = x
        self.Vy = y

    def execute(self, opcode):
        pass

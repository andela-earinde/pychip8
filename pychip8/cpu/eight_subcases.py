"""
This module contains the functions to execute
the eight opcode subcases
"""


def _zero_eight_execution(cpu, x, y):
    """
    Set Vx = Vy.
    Stores the value of register Vy in register Vx.
    """
    cpu.log("Set Vx = Vy")
    cpu.Vx[x] = cpu.Vx[y]


def _first_eight_execution(cpu, x, y):
    """
    Set Vx = Vx OR Vy.
    Performs a bitwise OR on the values of Vx and Vy, then stores the
    result in Vx. A bitwise OR compares the corrseponding bits from
    two values, and if either bit is 1, then the same bit in the result
    is also 1. Otherwise, it is 0.
    """
    cpu.log("Set Vx = Vx OR Vy")
    cpu.Vx[x] = cpu.Vx[x] | cpu.Vx[y]


def _second_eight_execution(cpu, x, y):
    """
    Set Vx = Vx AND Vy.
    Performs a bitwise AND on the values of Vx and Vy, then stores
    the result in Vx. A bitwise AND compares the corrseponding bits
    from two values, and if both bits are 1, then the same bit in
    the result is also 1. Otherwise, it is 0.
    """
    cpu.log("Set Vx = Vx AND Vy")
    cpu.Vx[x] = cpu.Vx[x] & cpu.Vx[y]


def _third_eight_execution(cpu, x, y):
    """
    Set Vx = Vx XOR Vy.
    Performs a bitwise exclusive OR on the values of Vx and Vy, then
    stores the result in Vx. An exclusive OR compares thecorrseponding
    bits from two values, and if the bits are not both the same, then
    the corresponding bit in the result is set to 1. Otherwise, it is 0.
    """
    cpu.log("Set Vx = Vx XOR Vy")
    cpu.Vx[x] = cpu.Vx[x] ^ cpu.Vx[y]


def _fourth_eight_execution(cpu, x, y):
    """
    Set Vx = Vx + Vy, set VF = carry.
    The values of Vx and Vy are added together. If the result is greater
    than 8 bits (i.e., > 255,) VF is set to 1, otherwise 0. Only the
    lowest 8 bits of the result are kept, and stored in Vx.
    """
    cpu.log("Set Vx = Vx + Vy, set VF = carry")
    sum = cpu.Vx[x] + cpu.Vx[y]

    if sum > 0xff:
        cpu.Vx[0xf] = 1
    else:
        cpu.Vx[0xf] = 0

    cpu.Vx[x] = sum


def _fifth_eight_execution(cpu, x, y):
    """
    Set Vx = Vx - Vy, set VF = NOT borrow.
    If Vx > Vy, then VF is set to 1, otherwise 0. Then Vy is subtracted
    from Vx, and the results stored in Vx.
    """
    cpu.log("Set Vx = Vx - Vy, set VF = NOT borrow")
    if cpu.Vx[x] > cpu.Vx[y]:
        cpu.Vx[0xf] = 1
    else:
        cpu.Vx[0xf] = 0

    cpu.Vx[x] = cpu.Vx[x] - cpu.Vx[y]


def _sixth_eight_execution(cpu, x, y):
    """
    Set Vx = Vx SHR 1.
    If the least-significant bit of Vx is 1, then VF is set
    to 1, otherwise 0. Then Vx is divided by 2.
    """
    cpu.log("Set Vx = Vx SHR 1")
    cpu.Vx[0xf] = cpu.Vx[x] & 0x01
    cpu.Vx[x] = cpu.Vx[x] >> 1


def _seventh_eight_execution(cpu, x, y):
    """
    Set Vx = Vy - Vx, set VF = NOT borrow.
    If Vy > Vx, then VF is set to 1, otherwise 0. Then Vx
    is subtracted from Vy, and the results stored in Vx.
    """
    cpu.log("Set Vx = Vy - Vx, set VF = NOT borrow")
    if cpu.Vx[x] > cpu.Vx[y]:
        cpu.Vx[0xf] = 0
    else:
        cpu.Vx[0xf] = 1

    cpu.Vx[x] = cpu.Vx[y] - cpu.Vx[x]


def _eight_eight_execution(cpu, x, y):
    """
    Set Vx = Vx SHL 1.
    If the most-significant bit of Vx is 1, then VF is set to 1,
    otherwise to 0. Then Vx is multiplied by 2.
    """
    cpu.log("Set Vx = Vx SHL 1")
    cpu.Vx[0xf] = cpu.Vx[x] & 0x80
    cpu.Vx[x] = cpu.Vx[x] << 1

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

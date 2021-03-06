"""
This module contains the functions to execute
the f opcode subcases
"""


def _first_f_execution(cpu, x, y):
    """
    Set Vx = delay timer value.
    The value of DT is placed into Vx.
    """
    cpu.log("Set Vx = delay timer value")
    cpu.Vx[x] = cpu.delay_timer


def _second_f_execution(cpu, x, y):
    """
    Wait for a key press, store the value of the key in Vx.
    All execution stops until a key is pressed, then the value
    of that key is stored in Vx.
    """
    cpu.log("Wait for a key press, store the value of the key in Vx")
    cpu.stop_cycle()
    # cpu.continue_cycle()


def _third_f_execution(cpu, x, y):
    """
    Set delay timer = Vx.
    DT is set equal to the value of Vx.
    """
    cpu.log("Set delay timer = Vx")
    cpu.delay_timer = cpu.Vx[x]


def _fourth_f_execution(cpu, x, y):
    """
    Set sound timer = Vx.
    ST is set equal to the value of Vx.
    """
    cpu.log("Set sound timer = Vx")
    cpu.sound_timer = cpu.Vx[x]


def _fifth_f_execution(cpu, x, y):
    """
    Set I = I + Vx.
    The values of I and Vx are added, and the results are stored in I.
    """
    cpu.log("Set I = I + Vx")
    cpu.I += cpu.Vx[x]
    if cpu.I > 0xfff:
        cpu.Vx[0xf] = 1
        cpu.I &= 0xfff
    else:
        cpu.Vx[0xf] = 0


def _sixth_f_execution(cpu, x, y):
    """
    Set I = location of sprite for digit Vx.
    The value of I is set to the location for the hexadecimal sprite
    correspondingto the value of Vx. See section 2.4, Display, for more
    information on the Chip-8 hexadecimal font.
    """
    cpu.log("Set I = location of sprite for digit Vx")
    cpu.I = (cpu.Vx[x] * 5) & 0xfff


def _seventh_f_execution(cpu, x, y):
    """
    Store BCD representation of Vx in memory locations I, I+1, and I+2.
    The interpreter takes the decimal value of Vx, and places the hundreds
    digit in memory at location in I, the tens digit at location I+1, and the
    ones digit at location I+2.
    """
    cpu.log("Store BCD representation of Vx in memory locations I, I+1, and I+2")
    for i, j in enumerate(str(cpu.Vx[x])):
        cpu.memory[cpu.I + i] = int(j)


def _eight_f_execution(cpu, x, y):
    """
    Store registers V0 through Vx in memory starting at location I.
    The interpreter copies the values of registers V0 through Vx into
    memory, starting at the address in I.
    """
    cpu.log("Store registers V0 through Vx in memory starting at location I")
    for i in xrange(x + 1):
        cpu.memory[cpu.I + i] = cpu.Vx[i]
    cpu.I += (x + 1)


def _ninth_f_execution(cpu, x, y):
    """
    Read registers V0 through Vx from memory starting at location I.
    The interpreter reads values from memory starting at location I
    into registers V0 through Vx.
    """
    cpu.log("Read registers V0 through Vx from memory starting at location I")
    for i in xrange(x + 1):
        cpu.Vx[i] = cpu.memory[cpu.I + i]
    cpu.I += (x + 1)


f_subcases = {
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

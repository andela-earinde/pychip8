"""
This module contains the functions to execute
the e opcode subcases
"""


def _zero_e_execution(cpu, x):
    """
    Skip next instruction if key with the value of Vx is pressed.
    Checks the keyboard, and if the key corresponding to the value of
    Vx is currently in the down position, PC is increased by 2.
    """
    cpu.log("Skip next instruction if key with the value of Vx is pressed")
    if cpu.keys[cpu.Vx[x]]:
        cpu.pc += 2


def _first_e_execution(cpu, x):
    """
    Skip next instruction if key with the value of Vx is not pressed.
    Checks the keyboard, and if the key corresponding to the value of
    Vx is currently in the up position, PC is increased by 2.
    """
    cpu.log("Skip next instruction if key with the value of Vx is not pressed")
    if not cpu.keys[cpu.Vx[x]]:
        cpu.pc += 2

e_subcases = {
    0x009e: _zero_e_execution,
    0x00a1: _first_e_execution
}

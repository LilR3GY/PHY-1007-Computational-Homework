import unittest

from src.circuit import Circuit
from src.wire import Current, Wire
from src.world import World


class TestWorld(unittest.TestCase):

    WORLD_SHAPE = (51, 51)

    WIRES = [
        Wire(start=(25, 13), stop=(13, 13), current=Current(x=0, y=1), voltage=4.5),
        Wire(start=(13, 13), stop=(13, 37), current=Current(x=1, y=0), voltage=4.5),
        Wire(start=(13, 37), stop=(25, 37), current=Current(x=0, y=-1), voltage=4.5),
        Wire(start=(25, 37), stop=(37, 37), current=Current(x=0, y=-1), voltage=-4.5),
        Wire(start=(37, 37), stop=(37, 13), current=Current(x=-1, y=0), voltage=-4.5),
        Wire(start=(37, 13), stop=(25, 13), current=Current(x=0, y=1), voltage=-4.5),
    ]
    CIRCUIT = Circuit(wires=WIRES)

    world = World(WORLD_SHAPE)
    world.place(CIRCUIT)
    world.compute()
    world.show_all()
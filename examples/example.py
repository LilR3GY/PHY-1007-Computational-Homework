import env_examples  # Modifies path, DO NOT REMOVE

from src import Circuit, Current, Wire, World


if __name__ == "__main__":
    #world = World(shape=(99, 99))  #Circuit A et Circuit B
    #world = World(shape=(149, 149))  #Circuit C
    world = World(shape=(85, 85))  #Circuit E
    
#                                 Circuit A
    wires_A = [
        Wire(start=(49, 24), stop=(24, 24), current=Current(x=-1, y=0), voltage=4.5),
        Wire(start=(24, 24), stop=(24, 75), current=Current(x=0, y=1), voltage=4.5),
        Wire(start=(24, 75), stop=(49, 75), current=Current(x=1, y=0), voltage=4.5),
        Wire(start=(49, 75), stop=(75, 75), current=Current(x=1, y=0), voltage=-4.5),
        Wire(start=(75, 75), stop=(75, 24), current=Current(x=0, y=-1), voltage=-4.5),
        Wire(start=(75, 24), stop=(49, 24), current=Current(x=-1, y=0), voltage=-4.5),
    ]
#                                 Circuit B
    wires_B =[
        Wire(start=(29, 24), stop=(24, 24), current=Current(x=-1, y=0), voltage=4.5),
        Wire(start=(24, 24), stop=(24, 75), current=Current(x=0, y=1), voltage=4.5),
        Wire(start=(24, 75), stop=(70, 75), current=Current(x=1, y=0), voltage=4.5),
        Wire(start=(70, 75), stop=(75, 75), current=Current(x=1, y=0), voltage=-4.5),
        Wire(start=(75, 75), stop=(75, 24), current=Current(x=0, y=1), voltage=-4.5),
        Wire(start=(75, 24), stop=(29, 24), current=Current(x=-1, y=0), voltage=-4.5),    
    ]
#                                 Circuit C
    wires_C = [
        Wire(start=(120, 49), stop=(24, 49), current=Current(x=-1, y=0), voltage=4.5),
        Wire(start=(24, 49), stop=(24, 100), current=Current(x=0, y=1), voltage=4.5),
        Wire(start=(24, 100), stop=(120, 100), current=Current(x=1, y=0), voltage=4.5),
        Wire(start=(120, 100), stop=(125, 100), current=Current(x=1, y=0), voltage=-4.5),
        Wire(start=(125, 100), stop=(125, 49), current=Current(x=0, y=-1), voltage=-4.5),
        Wire(start=(125, 49), stop=(120, 49), current=Current(x=-1, y=0), voltage=-4.5),
    ]
#                                 Circuit E
    wires_E = [
        Wire(start=(50, 40), stop=(50, 45), current=Current(x=0, y=1), voltage=4.5),
        Wire(start=(50, 45), stop=(20, 45), current=Current(x=-1, y=0), voltage=4.5),
        Wire(start=(20, 45), stop=(20, 55), current=Current(x=0, y=1), voltage=4.5),
        Wire(start=(20, 55), stop=(50, 55), current=Current(x=1, y=0), voltage=4.5),
        Wire(start=(50, 55), stop=(50, 60), current=Current(x=0, y=1), voltage=4.5),
        Wire(start=(50, 60), stop=(50, 65), current=Current(x=0, y=1), voltage=-4.5),
        Wire(start=(50, 65), stop=(15, 65), current=Current(x=-1, y=0), voltage=-4.5),
        Wire(start=(15, 65), stop=(15, 40), current=Current(x=0, y=-1), voltage=-4.5),
        Wire(start=(15, 40), stop=(15, 15), current=Current(x=0, y=-1), voltage=4.5),
        Wire(start=(15, 15), stop=(50, 15), current=Current(x=1, y=0), voltage=4.5),
        Wire(start=(50, 15), stop=(50, 20), current=Current(x=0, y=1), voltage=4.5),
        Wire(start=(50, 20), stop=(50, 25), current=Current(x=0, y=1), voltage=-4.5),
        Wire(start=(50, 25), stop=(20, 25), current=Current(x=-1, y=0), voltage=-4.5),   
        Wire(start=(20, 25), stop=(20, 35), current=Current(x=0, y=1), voltage=-4.5),
        Wire(start=(20, 35), stop=(50, 35), current=Current(x=1, y=0), voltage=-4.5),
        Wire(start=(50, 35), stop=(50, 40), current=Current(x=0, y=1), voltage=-4.5),
    ]

    circuit = Circuit(wires=wires_E)

    world.place(circuit)

    world.compute()

    world.show_all()

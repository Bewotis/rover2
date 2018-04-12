from rover import Rover


class RoverTestCase():
    # initial creation of the roverobject:
    rover = Rover(0, 0, 'N')

    givecommands = ['f', 'r', 'f', 'f']  # these are the commands that should be executed
    Rover.readcommands(rover, givecommands)
    Rover.giveroverlocation(rover)

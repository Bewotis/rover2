from rover import Rover


class RoverTest:

    # initial creation of the roverobject
    rover = Rover(0, 0, 'N')
    Rover.giveroverlocation(rover)

    givecommands = ['f', 'f', 'r', 'f']  # these are the commands that should be executed
    Rover.readcommands(rover, givecommands)
    Rover.giveroverlocation(rover)

from rover import Rover
from planet import Planet


class RoverTestCase():
    # initial creation of the roverobject:
    planet = Planet(5, 5)
    planet.addobstacle(0, 1)
    rover = Rover(0, 0, 'N', planet)

    givecommands = ['f', 'f', 'f', 'l', 'f', 'f', 'f']  # these are the commands that should be executed
    Rover.readcommands(rover, givecommands, planet)
    Rover.giveroverlocation(rover)

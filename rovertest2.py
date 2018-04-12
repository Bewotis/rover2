from rover import Rover
from planet import Planet


class RoverTestCase:
    # initial creation of the roverobject:
    planet = Planet(100, 100)
    planet.addobstacle(0, 1)
    rover = Rover(0, 0, 'N', planet)

    givecommands = ['f', 'f', 'r', 'f', 'f']  # these are the commands that should be executed
    Rover.readcommands(rover, givecommands, planet)
    Rover.giveroverlocation(rover)

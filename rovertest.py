import unittest
from rover import Rover
from planet import Planet


class RoverTestCase(unittest.TestCase):
    # initial creation of the roverobject
    def test_will_rover_move(self):
        planet = Planet(10, 10)
        rover = Rover(0, 0, 'N', planet)

        givecommands = ['f', 'r', 'f', 'f']  # these are the commands that should be executed
        # Rover.readcommands(rover, givecommands)
        # Rover.giveroverlocation(rover)
        self.assertTrue(Rover.readcommands(rover, givecommands, planet), msg=Rover.giveroverlocation(rover))

    def test_will_rover_refuse_unknown_commands(self):
        planet = Planet(10, 10)
        rover = Rover(0, 0, 'N', planet)

        givecommands = ['s', 'n', 'a', 'r']  # these are the commands that should be executed
        # Rover.readcommands(rover, givecommands)
        # Rover.giveroverlocation(rover)
        self.assertTrue(Rover.readcommands(rover, givecommands, planet), msg=Rover.giveroverlocation(rover))

    def test_will_rover_refuse_numeric_commands(self):
        planet = Planet(10, 10)
        rover = Rover(0, 0, 'N', planet)

        givecommands = [3, 2, 5.2, 'r']  # these are the commands that should be executed
        # Rover.readcommands(rover, givecommands)
        # Rover.giveroverlocation(rover)
        self.assertTrue(Rover.readcommands(rover, givecommands, planet), msg=Rover.giveroverlocation(rover))


if __name__ == '__main__':
    unittest.main()

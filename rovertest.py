import unittest
from rover import Rover


class RoverTestCase(unittest.TestCase):
    # initial creation of the roverobject
    def test_will_rover_move(self):
        rover = Rover(0, 0, 'N')

        givecommands = ['f', 'r', 'f', 'f']  # these are the commands that should be executed
        # Rover.readcommands(rover, givecommands)
        # Rover.giveroverlocation(rover)
        self.assertTrue(Rover.readcommands(rover, givecommands))


if __name__ == '__main__':
    unittest.main()
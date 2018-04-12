import unittest
from rover import Rover
from planet import Planet


class RoverTestCase(unittest.TestCase):
    # initial creation of the roverobject

    def setUp(self):  # creating same planet and rover for each test case
        self.planet = Planet(10, 10)
        self.rover = Rover(0, 0, 'N', self.planet)

    def tearDown(self):
        print('\n \n')

    def test_will_rover_move(self):
        givecommands = ['f', 'r', 'f', 'f']  # these are the commands that should be executed
        # Rover.readcommands(rover, givecommands)
        # Rover.giveroverlocation(rover)
        self.assertTrue(Rover.readcommands(self.rover, givecommands, self.planet), msg=Rover.giveroverlocation(self.rover))

    def test_will_rover_refuse_unknown_commands(self):
        givecommands = ['s', 'n', 'a', 'r']  # these are the commands that should be executed
        # Rover.readcommands(rover, givecommands)
        # Rover.giveroverlocation(rover)
        self.assertTrue(Rover.readcommands(self.rover, givecommands, self.planet), msg=Rover.giveroverlocation(self.rover))

    def test_will_rover_refuse_numeric_commands(self):
        givecommands = [3, 2, 5.2, 'r']  # these are the commands that should be executed
        # Rover.readcommands(rover, givecommands)
        # Rover.giveroverlocation(rover)
        self.assertTrue(Rover.readcommands(self.rover, givecommands, self.planet), msg=Rover.giveroverlocation(self.rover))


if __name__ == '__main__':
    unittest.main()

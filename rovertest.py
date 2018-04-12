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
        self.assertTrue(Rover.readcommands(self.rover, givecommands, self.planet), msg=Rover.giveroverlocation(self.rover))

    def test_will_rover_refuse_unknown_commands(self):
        givecommands = ['s', 'n', 'a', 'r']  # these are the commands that should be executed
        self.assertTrue(Rover.readcommands(self.rover, givecommands, self.planet), msg=Rover.giveroverlocation(self.rover))

    def test_will_rover_refuse_numeric_commands(self):
        givecommands = [3, 2, 5.2, 'r']  # these are the commands that should be executed
        self.assertTrue(Rover.readcommands(self.rover, givecommands, self.planet), msg=Rover.giveroverlocation(self.rover))

    def test_will_rover_stop_at_obstacle(self):
        self.planet.addobstacle(1, 2)
        givecommands = ['f', 'f', 'r', 'f', 'f', 'b']
        self.assertTrue(Rover.readcommands(self.rover, givecommands, self.planet), msg=Rover.giveroverlocation(self.rover))

    def test_will_false_obstacle_input_be_ignored(self):
        self.planet.addobstacle('sboj', 'adbiun')
        givecommands = ['f', 'f', 'r', 'f', 'f', 'b']
        self.assertTrue(Rover.readcommands(self.rover, givecommands, self.planet), msg=Rover.giveroverlocation(self.rover))

    def test_does_wrapping_work(self):
        givecommands = ('l', 'f')
        self.assertTrue(Rover.readcommands(self.rover, givecommands, self.planet), msg=Rover.giveroverlocation(self.rover))


if __name__ == '__main__':
    unittest.main()

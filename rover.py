class Rover:

    def __init__(self, x, y, orientation, planet):
        if planet.maxx >= x >= 0:  # checks if x coordinate is on the planet
            self.x = x

        else:
            print('your x coordinate: %d is not on the planet grid it has been placed at x=0' % x)
            self.x = 0

        if planet.maxy >= y >= 0:  # checks if y coordinate is on the planet
            self.y = y

        else:
            print('your y coordinate: %d is not on the planet grid it has been placed at y=0' % y)
            self.y = 0

        if orientation in ('N', 'E', 'S', 'W'):  # checks if orientation is valid
            self.orientation = orientation

        else:
            print('Your orientation does not match an actual orientation (N, E, S, W) the rover is now facing North')
            self.orientation = 'N'

        print('-------------------------------')

    def readcommands(self, commands, planet):  # function to read the commands and execute the corresponding functions
        for val in commands:
            self.giveroverlocation()
            print('-------------------------------')
            if self.orientation == 'N':

                if val == 'f':
                    self.y += 1

                    if [self.x, self.y] in planet.obstaclelist:  # checks if the rover encounters an obstacle
                        print('the rover encountered an obstacle on {}:{} and stopped it\'s movement'.format(self.x, self.y))
                        self.y -= 1
                        return True

                elif val == 'b':
                    self.y -= 1

                    if [self.x, self.y] in planet.obstaclelist:
                        print('the rover encountered an obstacle on {}:{} and stopped it\'s movement'.format(self.x, self.y))
                        self.y += 1
                        return True

                elif val == 'r':
                    self.orientation = 'E'

                elif val == 'l':
                    self.orientation = 'W'

                else:
                    print('invalid command %s' % val)

            elif self.orientation == 'E':

                if val == 'f':
                    self.x += 1

                    if [self.x, self.y] in planet.obstaclelist:
                        print('the rover encountered an obstacle on {}:{} and stopped it\'s movement'.format(self.x, self.y))
                        self.x -= 1
                        return True

                elif val == 'b':
                    self.x -= 1

                    if [self.x, self.y] in planet.obstaclelist:
                        print('the rover encountered an obstacle on {}:{} and stopped it\'s movement'.format(self.x, self.y))
                        self.x += 1
                        return True

                elif val == 'r':
                    self.orientation = 'S'

                elif val == 'l':
                    self.orientation = 'N'

                else:
                    print('invalid command %s' % val)

            elif self.orientation == 'S':

                if val == 'f':
                    self.y -= 1

                    if [self.x, self.y] in planet.obstaclelist:
                        print('the rover encountered an obstacle on {}:{} and stopped it\'s movement'.format(self.x, self.y))
                        self.y += 1

                        return True

                elif val == 'b':
                    self.y += 1

                    if [self.x, self.y] in planet.obstaclelist:
                        print('the rover encountered an obstacle on {}:{} and stopped it\'s movement'.format(self.x, self.y))
                        self.y -= 1
                        return True

                elif val == 'r':
                    self.orientation = 'W'

                elif val == 'l':
                    self.orientation = 'E'

                else:
                    print('invalid command %s' % val)

            elif self.orientation == 'W':

                if val == 'f':
                    self.x -= 1

                    if [self.x, self.y] in planet.obstaclelist:
                        print('the rover encountered an obstacle on {}:{} and stopped it\'s movement'.format(self.x, self.y))
                        self.x += 1
                        return True

                elif val == 'b':
                    self.x += 1

                    if [self.x, self.y] in planet.obstaclelist:
                        print('the rover encountered an obstacle on {}:{} and stopped it\'s movement'.format(self.x, self.y))
                        self.x -= 1
                        return True

                elif val == 'r':
                    self.orientation = 'N'

                elif val == 'l':
                    self.orientation = 'S'

                else:
                    print('invalid command %s' % val)

        return True
        # print('The rover is on %d : %d facing %s' % (self.x, self.y, self.orientation))

    def giveroverlocation(self):
        print('The rover is on %d : %d facing %s' % (self.x, self.y, self.orientation))
        print('-------------------------------')


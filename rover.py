class Rover:

    def __init__(self, x, y, orientation):
        self.x = x
        self.y = y
        self.orientation = orientation

    '''def forward(self):
        if self.orientation == 'N' or 'n':
            self.y += 1

        elif self.orientation == 'E' or 'e':
            self.x += 1

        elif self.orientation == 'S' or 's':
            self.y -= 1

        elif self.orientation == 'W' or 'w':
            self.x -= 1

    def backward(self):
        if self.orientation == 'N' or 'n':
            self.y -= 1

        elif self.orientation == 'E' or 'e':
            self.x -= 1

        elif self.orientation == 'S' or 's':
            self.y += 1

        elif self.orientation == 'W' or 'w':
            self.x += 1

    def turnleft(self):
        if self.orientation == 'N' or 'n':
            self.orientation = 'W'

        elif self.orientation == 'E' or 'e':
            self.orientation = 'N'

        elif self.orientation == 'S' or 's':
            self.orientation = 'E'

        elif self.orientation == 'W' or 'w':
            self.orientation = 'S'

    def turnright(self):
        if self.orientation == 'N' or 'n':
            self.orientation = 'E'

        elif self.orientation == 'E' or 'e':
            self.orientation = 'S'

        elif self.orientation == 'S' or 's':
            self.orientation = 'W'

        elif self.orientation == 'W' or 'w':
            self.orientation = 'N'''''

    def readcommands(self, commands):  # function to read the commands and execute the corresponding functions
        for val in commands:

            if self.orientation == 'N' or 'n':

                if val == 'f':
                    self.y += 1

                elif val == 'b':
                    self.y -= 1

                elif val == 'r':
                    self.orientation = 'E'

                elif val == 'l':
                    self.orientation = 'W'

            elif self.orientation == 'E' or 'e':

                if val == 'f':
                    self.x += 1

                elif val == 'b':
                    self.x -= 1

                elif val == 'r':
                    self.orientation = 'S'

                elif val == 'l':
                    self.orientation = 'N'

            elif self.orientation == 'S' or 's':

                if val == 'f':
                    self.y -= 1

                elif val == 'b':
                    self.y += 1

                elif val == 'r':
                    self.orientation = 'W'

                elif val == 'l':
                    self.orientation = 'E'

            elif self.orientation == 'W' or 'w':

                if val == 'f':
                    self.x -= 1

                elif val == 'b':
                    self.x += 1

                elif val == 'r':
                    self.orientation = 'N'

                elif val == 'l':
                    self.orientation = 'S'
        #print('The rover is on %d : %d facing %s' % (self.x, self.y, self.orientation))

    def giveroverlocation(self):
        print('The rover is on %d : %d facing %s' % (self.x, self.y, self.orientation))


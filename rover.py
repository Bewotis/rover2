class Rover:

    def __init__(self, x, y, orientation):
        self.x = x
        self.y = y
        self.orientation = orientation

    def forward(self):
        if self.orientation == 'N' or 'n':
            self.x += 1

        elif self.orientation == 'E' or 'e':
            self.y += 1

        elif self.orientation == 'S' or 's':
            self.x -= 1

        elif self.orientation == 'W' or 'w':
            self.y -= 1

    def backward(self):
        if self.orientation == 'N' or 'n':
            self.x -= 1

        elif self.orientation == 'E' or 'e':
            self.y -= 1

        elif self.orientation == 'S' or 's':
            self.x += 1

        elif self.orientation == 'W' or 'w':
            self.y += 1

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
            self.orientation = 'N'

    def readcommands(self, commands):  # function to read the commands and execute the corresponding functions
        for x in commands:

            if x == 'f':
                self.forward()

            elif x == 'b':
                self.backward()

            elif x == 'r':
                self.turnright()

            elif x == 'l':
                self.turnleft()

    def giveroverlocation(self):
        print('The rover is on %d : %d facing %s' % (self.x, self.y, self.orientation))


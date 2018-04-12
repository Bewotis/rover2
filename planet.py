class Planet:

    def __init__(self, maxx, maxy):
        self.maxx = maxx
        self.maxy = maxy
        self.obstaclelist = []

    def addobstacle(self, obstaclex, obstacley):
        if obstaclex == int and obstacley == int:
            obstacle = [obstaclex, obstacley]
            self.obstaclelist.append(obstacle)
            return True
        else:
            print('!!!ERROR!!! \n the coordinates for the obstacle are wrong. The obstacle has not been created'
                  '\n-------------------------------')
            return False

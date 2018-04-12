class Planet:

    def __init__(self, maxx, maxy):
        self.maxx = maxx
        self.maxy = maxy
        self.obstaclelist = []

    def addobstacle(self, obstaclex, obstacley):
        obstacle = [obstaclex, obstacley]
        self.obstaclelist.append(obstacle)

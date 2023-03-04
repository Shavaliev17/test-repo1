class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def dist(self, point):
        distance = (self.x ** 2 + self.y ** 2) ** (1/2)
        return distance



#Team Afro Dog
#@Shivam Swarnkar
#Coordinate Class

class Coordinate:
    def __init__(self, x, y, x_inc = 0, y_inc = 0):
        self.x = x
        self.y = y
        self.x_inc = x_inc
        self.y_inc = y_inc

    def x(self):
        return self.x
    def y(self):
        return self.y
    def x_change(self, x):
        self.x = x
    def y_change(self, y):
        self.y = y
    def x_inc_change(self, x):
        self.x_inc = x
    def y_inc_change(self, y):
        self.y_inc = y
    def inc_change(self, x, y):
        self.x_inc = x
        self.y_inc = y
    def x_inc(self):
        return self.x_inc
    def y_inc(self):
        return self.y_inc
    def incrX(self):
        self.x += self.x_inc
    def incrY(self):
        self.y += self.y_inc
    def inc(self):
        self.x += self.x_inc
        self.y += self.y_inc
    


    

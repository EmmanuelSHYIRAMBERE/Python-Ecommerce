class Point:
    def __init__(self, x,y):
        self.x=x
        self.y=y
    def draw(self):
        print("Draw")

point = Point(10,20)
print(point.x)
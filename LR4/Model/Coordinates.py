class Coordinates:
    def __init__(self, x, y):
        self.__x: int = x
        self.__y: int = y
    
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y
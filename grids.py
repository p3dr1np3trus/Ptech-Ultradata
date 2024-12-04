class Grid2d:
    def __init__(self, xSize: int, items: list):
        self.Xsize = xSize
        self.items = items

        if len(self.items) % self.Xsize != 0:
            self.Xsize = len(self.items)

        self.content = [
            self.items[i:i + self.Xsize] for i in range(0, len(self.items), self.Xsize)
        ]


    def printDebug(self):
        for item in self.content:
            print(item)
    
    def getItem(self, x, y):
        return self.content[y][x]


class Grid3d:
    def __init__(self, xSize: int, Ysize: int, items: list):
        self.Xsize = xSize
        self.Zsize = Ysize
        self.items = items
        if len(self.items) % self.Xsize != 0:
            self.Xsize = len(self.items)
            self.Zsize = 1
        elif len(self.items) % self.Zsize != 0:
            self.Zsize = len(self.items)
            self.Xsize = 1


        self.content = []
        iterator = 0

        for z in range(Ysize):
            layer = []
            for x in range(xSize):  
                row = items[iterator:iterator + xSize] 
                layer.append(row)
                iterator += xSize
            self.content.append(layer)

    def printDebug(self):
        for row in self.content:
            print(row)

                            
    def getItem(self, row, col, layer):
        return self.content[col][layer][row]
        

def examplefunc():
    print("Grid2d:")
    Grid2d(3, ["a", "b", "c", "d", "e", "f", "g", "h", "i"]).printDebug()
    print("Grid3d:")
    Grid3d(2, 3, ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]).printDebug()


examplefunc()
print(Grid2d(3, ["a", "b", "c", "d", "e", "f", "g", "h", "i"]).getItem(2, 2))
print(Grid3d(2, 6, ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]).getItem(2, 2, 2))

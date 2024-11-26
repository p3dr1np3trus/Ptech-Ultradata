class AxisEnd:
    def __init__(self):
        self.property = "AxisEnd"

class Grid2d:
    def __init__(self, xSize: int, items: list):
        self.Xsize = xSize
        self.items = items
        if len(self.items) % self.Xsize != 0:
            self.Xsize = len(self.items)

    def printDebug(self):
        printcontent = []
        iterator = 0
        for item in self.items:
            printcontent.append(item)
            iterator += 1
            if len(printcontent) == self.Xsize:
                print(printcontent)
                printcontent = []
    
    def iterate(self):
        iterated = []
        for item in self.items:
            iterated.append(item)
            if len(iterated) % self.Xsize == 0:
                iterated.append(AxisEnd())
        return iterated
    
class Grid3d:
    def __init__(self, xSize: int, Zsize: int, items: list):
        self.Xsize = xSize
        self.Zsize = Zsize
        self.items = items
        if len(self.items) % self.Xsize != 0:
            self.Xsize = len(self.items)
            self.Zsize = 1
        elif len(self.items) % self.Zsize != 0:
            self.Zsize = len(self.items)
            self.Xsize = 1

    def printDebug(self):
        printcontent = []
        xprint = []
        for item in self.items:   
            xprint.append(item)
            if len(xprint) == self.Xsize:
                printcontent.append(xprint)
                xprint = []
                if len(printcontent) == self.Zsize:
                    print(printcontent)
                    printcontent = []

                            


def examplefunc():
    print("Grid2d:")
    Grid2d(3, ["a", "b", "c", "d", "e", "f", "g", "h", "i"]).printDebug()
    print("Grid3d:")
    Grid3d(2, 3, ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]).printDebug()
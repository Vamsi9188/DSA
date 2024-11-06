# ====================== CLASSES, OBJECTS AND PROPERTIES =============================#
class House:
    pass 

h1=House()
h1.windows=2
h1.doors=1

h2=House()
h2.windows=4
h2.doors=2

print(f"h1 has {h1.windows} windows and {h1.doors}")
print(f"h2 has {h2.windows} windows and {h2.doors}")


# ====================== CLASSES, OBJECTS AND PROPERTIES =============================#
class House:
    pass 

h1=House()
h1.windows=2
h1.doors=1

h2=House()
h2.windows=4
h2.doors=2

def printHouseProperties(h):
    print("House has",h.windows,"windows and",h.doors,"doors")

def addDoor(h):
    h.doors=h.doors+9
printHouseProperties(h1)
printHouseProperties(h2)
addDoor(h1)

# ====================== INSTANCE METHODS AND NORMAL FUNCIONS ============================= #
class ABC:
    pass
    def f1(x,y,z):
        print(x,y,z)
        if y!=0:
            x.f1(y-1,z)
a1=ABC()
a1.f1(1,2)

class XYZ:
    pass
    def f1(self,y,z):
        print(self,y,z)
        if y!=0:
            self.f1(y-1,z)
x1=XYZ()
x1.f1(12,21)


# =================================== DUNDER METHODS OR MAGIC METHODS ==================================== #
class ABC:
    def __init__(self):
        print("I am called")
        print("Bye Bye")
    def f1(self,y,z):
        print(self,y,z)
        if y!=0:
            self.f1(y-1,z)
print(1)
a1=ABC()
print(2)
a1.f1(1,2)


class House:
    def __init__(self,doors,windows):
        self.doors=doors
        self.windows=windows
    def houseProperties(self):
        print("House has",self.windows,"windows and",self.doors,"doors.")
    def addDoors(self):
        self.doors = self.doors+1
        
h1=House(4,2)
h1.addDoors()
h1.houseProperties()

h2=House(3,0)
h2.houseProperties()


class House:
    def __init__(self,windows=0,doors=0):
        self.windows=windows
        self.doors=doors
    def __str__(self):
        return f"House has {self.doors} doors and {self.windows} windows"
    def addDoors(self):
        self.doors = self.doors+1
        
h1=House(8,3)
h1.addDoors()
print(h1)
h2=House(4)
print(h2)



    
    
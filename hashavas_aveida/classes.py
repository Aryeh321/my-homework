class Aveidah:
    def __init__(self, name, color, size, shape, location):
        self.name = name
        self.color = color
        self.size = size
        self.shape = shape
        self.location = location

class AveidahFinder:
    def __init__(self):
        self.lost_objects = {Aveidah.name:"wallet", Aveidah.color:"brown", Aveidah.size:"small", Aveidah.shape:"one fold", Aveidah.location:"parking lot"}

    def siman_checker(self, name, color, size, shape, location):
        return name == aveidah.name and color == aveidah.color and size == aveidah.size and shape == aveidah.shape and location == aveidah.location

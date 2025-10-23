class Aveidah:
    def __init__(self, name, color, size, shape, location):
        self.name = name
        self.color = color
        self.size = size
        self.shape = shape
        self.location = location

class AveidahFinder:
    def __init__(self):
        self.lost_objects = [Aveidah(name="wallet", color="brown", size="small", shape="one fold", location="parking lot"),
                             Aveidah(name="sippy cup", color="blue", size="small", shape="round", location="shul"),
                             Aveidah(name="watch", color="silver", size="small", shape="round face", location="npgs"),
                             Aveidah(name="pen", color="green", size="small", shape="parker", location="park"),
]

    def siman_checker(self, name, color, size, shape, location):
        found_objects = []
        for obj in self.lost_objects:
            if obj.name == name and obj.color == color and obj.size == size and obj.shape == shape and obj.location == location:
                found_objects.append(obj)
        
        return found_objects

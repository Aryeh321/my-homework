from classes import AveidahFinder

finder = AveidahFinder()
matches = finder.siman_checker(name="wallet", color="brown", size="small", shape="one fold", location="parking lot")
for aveidah in matches:
    print(f"Found: {aveidah.name}")
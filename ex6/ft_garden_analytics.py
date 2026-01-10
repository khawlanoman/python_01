class Plant:
    
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self.growth = growth
        self.plant_type = plant_type



class FloweringPlant(Plant):
    def __init__(self, name, height,color):
        super.__init__(self,name, height)
        self.color = color


class PrizeFlower(FloweringPlant):
    def __init__(self,name,height,color,prize):
        super.__init__(self, prize)
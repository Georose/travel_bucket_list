class Country: 
    def __init__(self, name, visit = False, id = None):
        self.name = name
        self.cities = []
        self.visit = visit
        self.id = id
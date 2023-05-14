class Fridge:
    brand = "LG"
    model = "GW-B509SMUM"
    capacity = 384
    is_defrosting = False
    energy_efficiency_class = "A++"

    instance = None

    @staticmethod
    def get_instance():
        if Fridge.instance is None:
            Fridge.instance = Fridge()
        return Fridge.instance

    def turn_on_defrosting(self):
        self.is_defrosting = True

    def turn_off_defrosting(self):
        self.is_defrosting = False

    def delete_model_info(self):
        if self.model is None:
            print("The model information is already deleted.")
        else:
            self.model = None
            print("The model information has been deleted.")

    def __init__(self, brand=None, model=None, capacity=None, is_defrosting=None, energy_efficiency_class=None):
        if brand is not None:
            self.brand = brand
        if model is not None:
            self.model = model
        if capacity is not None:
            self.capacity = capacity
        if is_defrosting is not None:
            self.is_defrosting = is_defrosting
        if energy_efficiency_class is not None:
            self.energy_efficiency_class = energy_efficiency_class

    def __str__(self):
        return f"Brand: {self.brand}, Model: {self.model}, Capacity: {self.capacity}," \
               f" Defrosting: {self.is_defrosting}, Energy Efficiency Class: {self.energy_efficiency_class}"


if __name__ == "__main__":
    fridges = [
        Fridge(),
        Fridge("Samsung", "RB36T677FB1", 360, False, "A+"),
        Fridge.get_instance(),
        Fridge.get_instance()
    ]

    for fridge in fridges:
        fridge.turn_on_defrosting()
        fridge.turn_off_defrosting()
        fridge.delete_model_info()
        print(fridge)

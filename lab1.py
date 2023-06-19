class Fridge:
    brand = "LG"
    model = "GW-B509SMUM"
    capacity = 384
    is_defrosting = False
    energy_efficiency_class = "A++"

    instance = None

    def __init__(self, brand="Samsung", model="RB36T677FB1", capacity=360, is_defrosting=False,
                 energy_efficiency_class="A+"):
        self.brand = brand
        self.model = model
        self.capacity = capacity
        self.is_defrosting = is_defrosting
        self.energy_efficiency_class = energy_efficiency_class

    @staticmethod
    def get_instance():
        """
        this function is returning an instance of a class
        """
        if Fridge.instance is None:
            Fridge.instance = Fridge()
        return Fridge.instance

    def turn_on_defrosting(self):
        """
        this function is turning on defrosting
        """
        self.is_defrosting = True

    def turn_off_defrosting(self):
        """
        this function is turning off defrosting
        """
        self.is_defrosting = False

    def delete_model_info(self):
        """
        this function is deleting info about model of fridges
        """
        if self.model is None:
            print("The model information is already deleted.")
        else:
            self.model = None
            print("The model information has been deleted.")

    def __str__(self):
        return f"Brand: {self.brand}, Model: {self.model}, Capacity: {self.capacity}," \
               f" Defrosting: {self.is_defrosting}, Energy Efficiency Class: {self.energy_efficiency_class}"

    def __repr__(self):
        return f"Brand: {self.brand}, Model: {self.model}, Capacity: {self.capacity}," \
               f"Defrosting: {self.is_defrosting}, Energy Efficiency Class: {self.energy_efficiency_class}"


if __name__ == "__main__":
    fridges = [
        Fridge(),
        Fridge("Samsung", "RB36T677FB1", 360, False, "A+"),
        Fridge.get_instance(),
        Fridge.get_instance(),
    ]
    fridges2 = [
        Fridge("Xiaomi", "Note 10"),
        Fridge("Apple", "13"),
        Fridge("Samsung", "20A"),
        Fridge("Samsung", "15A"),
    ]

    for fridge in fridges:
        fridge.turn_on_defrosting()
        fridge.turn_off_defrosting()
        fridge.delete_model_info()
        print(fridge)

    half_length = len(fridges2) // 2
    fridges2_reversed = list(reversed(fridges2))
    for fridge in fridges2_reversed[:half_length]:
        print(fridge)

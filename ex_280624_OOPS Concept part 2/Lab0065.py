class Car:

    def __init__(self, OEM_name, OEM_make, OEM_model):
        self.name = OEM_name
        self.make = OEM_make
        self.model = OEM_model

    def start_engine(self):
        print("Starting a car with name ", self.name)
        print("Starting a car with make ", self.make)
        print("Starting a car with model ", self.model)


car1 = Car("Benz", 5200, "XYZ")
car1.start_engine()





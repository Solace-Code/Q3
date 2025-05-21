class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition: Engine is a part of Car

    def start_car(self):
        print("Starting the car...")
        self.engine.start()  # Accessing Engine method through Car

# Example usage:
my_engine = Engine()
my_car = Car(my_engine)

my_car.start_car()

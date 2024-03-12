
class Car:

    def __init__(self, model_name, year_of_release, manufacturer, engine_power, colour, price):
        self.model_name = model_name
        self.year_of_release = year_of_release
        self.manufacturer = manufacturer
        self.engine_power = engine_power
        self.colour = colour
        self.price = price

    def printer(self):
        print(self.model_name)
        print(self.year_of_release)
        print(self.manufacturer)
        print(self.engine_power)
        print(self.colour)
        print(self.price)


def __init__(self, model_name, year_of_release, manufacturer, engine_power, colour, price):
    def set_model_name(self, model_name):
        self.model_name = model_name

    def get_model_name(self):
        return self.model_name

    def set_year_of_release(self, year_of_release):
        self.year_of_release = year_of_release

    def get_year_of_release(self):
        return self.year_of_release


if __name__ == '__main__':
    auto = Car("X7 M50i", "2021", "BMW", "530 л.с.", "white", "10790000")
    auto.printer()






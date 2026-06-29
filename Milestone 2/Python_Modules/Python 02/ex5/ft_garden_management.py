class GardenError(Exception):
    pass


class PlantNameError(GardenError):
    pass


class WaterLevelError(GardenError):
    pass


class TankError(GardenError):
    pass


class GardenManager:

    def __init__(self):
        self.plants = {}

    def add_plant(self, name):
        if name == "":
            raise PlantNameError("Plant name cannot be empty!")
        self.plants[name] = {"water": 5, "sun": 8}
        print("Added", name, "successfully")

    def water_plants(self):
        print("Opening watering system")
        try:
            for plant in self.plants:
                print("Watering", plant, "- success")
        finally:
            print("Closing watering system (cleanup)")
        print()

    def check_plant_health(self, name, water, sun):
        if water > 10:
            msg = f"Water level {water} is too high (max 10)"
            raise WaterLevelError(msg)
        msg = f"{name}: healthy (water: {water}, sun: {sun})"
        print(msg)


def test_garden_management():
    garden = GardenManager()

    print("Adding plants to garden...")
    try:
        garden.add_plant("tomato")
        garden.add_plant("lettuce")
        garden.add_plant("")
    except GardenError as e:
        print("Error adding plant:", e)
    print()

    print("Watering plants...")
    garden.water_plants()

    print("Checking plant health...")
    try:
        garden.check_plant_health("tomato", 5, 8)
    except GardenError as e:
        print("Error checking tomato:", e)

    try:
        garden.check_plant_health("lettuce", 15, 7)
    except GardenError as e:
        print("Error checking lettuce:", e)
    print()

    print("Testing error recovery...")
    try:
        raise TankError("Not enough water in tank")
    except GardenError as e:
        print("Caught GardenError:", e)

    print("System recovered and continuing...")
    print()
    print("Garden management system test complete!")


if __name__ == "__main__":
    print("=== Garden Management System ===")
    print()
    test_garden_management()

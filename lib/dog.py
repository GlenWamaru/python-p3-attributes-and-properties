

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name, breed=""):
        self.name = name
        self.breed = breed

    def get_name(self):
        return self._name
    
    def set_name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            print(f"Setting name to {value}")
            self._name = value
        else:
            print("Name must be a string between 1 and 25 characters")    

    name = property(get_name, set_name)

    
    def breed(self):
        return self._breed

    def breed(self, value):
        if value in APPROVED_BREEDS:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")

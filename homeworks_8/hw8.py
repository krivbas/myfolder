class Animals:
    def __init__(self, size, voice):
        self.size = size
        self.voice = voice

    def get_voice_animals_method(self):
        raise NotImplementedError("No method")


class WildAnimals(Animals):
    """my class"""
    def __init__(self, size):
        self.size = size

class HomeAnimals(Animals):
    """my class"""
    def get_voice_animals_method(self):
        return"voice - {}".format(self.voice)



Cat = HomeAnimals("little", "myau")
Dog = HomeAnimals("midle", "gav")
Tiger = WildAnimals("big")
Wolf = WildAnimals("big")
Fox = WildAnimals("little")

print(Fox.get_voice_animals_method())

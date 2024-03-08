class Owner:
    def __init__(self, name):
        self.name = name
        self.pets_list = []

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Not a valid pet type")
        pet.set_owner(self)
        self.pets_list.append(pet)

    def get_sorted_pets(self):
        return sorted(self.pets_list, key=lambda x: x.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all_pets = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type")
        self.owner = owner
        self.set_owner(owner)
        self.all_pets.append(self)

    def set_owner(self, owner):
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Not a valid owner type")
        self.owner = owner

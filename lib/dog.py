#!/usr/bin/env python3



class Dog: 
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

    def __init__(self, name="Fido", breed="Corgi"):
        if isinstance(name, str) and 1 <= len(name) <= 25 and name != "":
            self._name = name.title()  
        else:
            print("Name must be string between 1 and 25 characters.")
        
        if breed in self.APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")

    
    def get_name(self):
        print("Retrieving name")
        return self._name
    
    def set_name(self, name):
        if isinstance(name, str) and 1 < len(name) <  25 and name != "":
            self._name = name.title()  
        else:
            print("Name must be string between 1 and 25 characters.")
    
    def get_breed(self):
        print("Retrieving breed")
        return self._breed 
    
    def set_breed(self, breed):
        if breed in self.APPROVED_BREEDS and isinstance(breed, str):
            self._breed = breed
            print(breed)
        else:
            print("Breed must be in list of approved breeds.")

    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)


# fido = Dog()
# fido.name = "fido"
# fido.breed = "Mutt"

# print(fido.name)
# print(fido.breed)





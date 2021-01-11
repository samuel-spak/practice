class oak():
    def __init__(self,pokemon):
        self.pokemon = pokemon

    def catchem(self):
        print(f'I choose you {self.pokemon}')

profOak = oak("pikachu")
kidOak = oak("mudkip")
kidOak.catchem()
print(profOak.pokemon)

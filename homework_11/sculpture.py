from art_object import ArtObject


class Sculpture(ArtObject):
    def __init__(self, title, author, material: str):
        super().__init__(title, author)
        self._material = material

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, new_material: str):
        self._material = new_material

    @classmethod
    def from_title(cls, title: str):
        return cls(title, 'Unknown', 'stone')

    def get_full_info(self):
        return f'{super().get_main_info()} \nMaterial: {self._material}'

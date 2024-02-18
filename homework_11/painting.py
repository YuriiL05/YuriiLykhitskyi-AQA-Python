from art_object import ArtObject


class Painting(ArtObject):

    def __init__(self, title, author, style: str):
        super().__init__(title, author)
        self._style = style

    @property
    def style(self):
        return self._style

    @style.setter
    def style(self, new_style: str):
        self._style = new_style

    def get_full_info(self):
        return f'{super().get_main_info()} \nStyle: {self._style}'



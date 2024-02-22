from abc import ABC, abstractmethod


class ArtObject(ABC):
    def __init__(self, title: str, author: str):
        self.__title = title
        self.__author = author

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @title.setter
    def title(self, new_title: str):
        self.__title = new_title

    @author.setter
    def author(self, new_author: str):
        if type(new_author) is str:
            self.__author = new_author
        else:
            raise TypeError('author must be a string')

    def get_main_info(self):
        return f'Art object: {self.__title} \nBy: {self.author}'

    @abstractmethod
    def get_full_info(self):
        pass

from .base_service import BaseService


class StarshipsService(BaseService):
    def __init__(self):
        super().__init__('starships')

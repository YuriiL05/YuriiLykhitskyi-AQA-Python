from .base_service import BaseService


class VehiclesService(BaseService):
    def __init__(self):
        super().__init__('vehicles')

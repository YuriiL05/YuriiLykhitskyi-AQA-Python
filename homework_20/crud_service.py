import requests


class CRUDService:
    base_url = 'https://api.restful-api.dev/objects'

    @staticmethod
    def get_list_of_all_objects():
        return requests.get(CRUDService.base_url)

    @staticmethod
    def get_list_of_objects_by_ids(object_ids: list):
        query_string = f'?id={object_ids[0]}'
        if object_ids.__len__() > 1:
            for object_id in object_ids[1:]:
                query_string += f'&id={object_id}'
        return requests.get(CRUDService.base_url + query_string)

    @staticmethod
    def get_object_by_id(_id):
        return requests.get(CRUDService.base_url + f'/{_id}')

    @staticmethod
    def add_object(object_data):
        return requests.post(CRUDService.base_url, json=object_data)

    @staticmethod
    def update_object(object_id, object_data):
        return requests.put(CRUDService.base_url + f'/{object_id}', json=object_data)

    @staticmethod
    def partially_update_object(object_id, object_data):
        return requests.patch(CRUDService.base_url + f'/{object_id}', json=object_data)

    @staticmethod
    def delete_object(object_id):
        return requests.delete(CRUDService.base_url + f'/{object_id}')

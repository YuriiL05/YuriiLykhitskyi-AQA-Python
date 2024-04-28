from .crud_service import CRUDService


def test_get_list_of_all_objects(test_data):
    response = CRUDService.get_list_of_all_objects()
    assert response.status_code == 200
    assert response.json() == test_data.all_data


def test_get_list_of_objects_by_ids(test_data):
    response = CRUDService.get_list_of_objects_by_ids([1, 3, 5])
    assert response.status_code == 200
    assert response.json() == test_data.get_list_by_ids([1, 3, 5])


def test_get_single_object_by_id(test_data):
    response = CRUDService.get_object_by_id(2)
    assert response.status_code == 200
    assert response.json() == test_data.get_single_object(2)


def test_add_object(test_data):
    response = CRUDService.add_object(test_data.set_add_object('add_phone'))
    assert response.status_code == 200
    assert response.json()['name'] == test_data.add_object['name']


def test_update_object(test_data):
    _id = CRUDService.add_object(test_data.set_add_object('add_phone')).json()['id']
    response = CRUDService.update_object(_id, test_data.set_update_object('update_phone'))
    assert response.status_code == 200
    assert response.json()['data'] == test_data.update_object['data']
    assert response.json()['updatedAt']


def test_partially_update_object(test_data):
    _id = CRUDService.add_object(test_data.set_add_object('add_phone')).json()['id']
    response = CRUDService.partially_update_object(_id, test_data.set_update_object('partially_update_phone'))
    assert response.status_code == 200
    assert response.json()['data'] == test_data.update_object['data']


def test_delete_object(test_data):
    _id = CRUDService.add_object(test_data.set_add_object('add_phone')).json()['id']
    response = CRUDService.delete_object(_id)
    assert response.status_code == 200
    assert response.json()['message'] == f'Object with id = {_id} has been deleted.'
    assert CRUDService.get_object_by_id(_id).status_code == 404

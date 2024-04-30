import requests
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table, func
from sqlalchemy.orm import sessionmaker


class ApiDbAdapter:
    def __init__(self, api_endpoint, db_url):
        self.api_endpoint = api_endpoint
        self.db_url = db_url
        self.engine = create_engine(db_url)
        self.session = sessionmaker(bind=self.engine)
        self.metadata = MetaData()
        self.device_table = Table(
            'device_table', self.metadata,
            Column('id', String),
            Column('name', String),
            Column('year', Integer),
            Column('price', String),
            Column('cpumodel', String),
            Column('harddisksize', String)
        )
        self.metadata.create_all(bind=self.engine)

    def post_get_insert_select(self, data):
        _id = self.post_object(data).json()['id']
        created_object = self.get_object_by_id(_id).json()
        self.insert_into_db(created_object)
        inserted_object = self.get_from_db(_id)
        return created_object, inserted_object

    def put_get_update_select(self, data, _id):
        self.put_object(_id, data)
        updated_object_api = self.get_object_by_id(_id)
        self.update_into_db(_id, data)
        updated_object_db = self.get_from_db(_id)
        return updated_object_api, updated_object_db

    def update_select_put_get(self, _id, data):
        self.update_into_db(_id, data)
        updated_object_db = self.get_from_db(_id)
        self.put_object(_id, data)
        updated_object_api = self.get_object_by_id(_id)
        return updated_object_db, updated_object_api

    def insert_into_db(self, data=None):
        session = self.session()
        new_item = self.device_table.insert().values(id=data['id'],
                                                     name=data['name'],
                                                     year=data['data']['year'],
                                                     price=data['data']['price'],
                                                     cpumodel=data['data']['CPU model'],
                                                     harddisksize=data['data']['Hard disk size'])
        session.execute(new_item)
        session.commit()
        session.close()

    def update_into_db(self, _id, data):
        session = self.session()
        new_item = self.device_table.update().where(self.device_table.c.id == _id).values(id=_id,
                                                                                          name=data['name'],
                                                                                          year=data['data']['year'],
                                                                                          price=data['data']['price'],
                                                                                          cpumodel=data['data'][
                                                                                              'CPU model'],
                                                                                          harddisksize=data['data'][
                                                                                              'Hard disk size'])
        session.execute(new_item)
        session.commit()
        session.close()

    def get_from_db(self, _id):
        session = self.session()
        query = self.device_table.select().where(self.device_table.c.id == _id)
        result = session.execute(query)
        rows = result.fetchall()
        session.close()
        return rows

    def get_object_by_id(self, _id):
        return requests.get(self.api_endpoint + f'/{_id}')

    def post_object(self, data):
        return requests.post(self.api_endpoint, json=data)

    def put_object(self, _id, data):
        return requests.put(self.api_endpoint + f'/{_id}', json=data)


if __name__ == '__main__':
    api_endpoint = 'https://api.restful-api.dev/objects'
    db_url = 'postgresql://yurii_l:12884@localhost:5432/postgres'  # Replace with your PostgreSQL connection URL
    adapter = ApiDbAdapter(api_endpoint, db_url)
    data_create = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    data_update = {
        "name": "Apple MacBook Pro 17",
        "data": {
            "year": 2020,
            "price": 1849.99,
            "CPU model": "Intel Core i7",
            "Hard disk size": "1 TB"
        }
    }

    api_db = adapter.post_get_insert_select(data_create)
    api_put_db = adapter.put_get_update_select(data_update, 'ff8081818f28dba8018f295aeb510244')
    db_api = adapter.update_select_put_get('ff8081818f28dba8018f295aeb510244', data_create)

    print("Object from API:", api_db)
    print("Object from API Put:", api_put_db)
    print("Object from SQL:", db_api)

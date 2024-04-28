class DataModel:
    def __init__(self, full_data):
        self.full_data = full_data
        self.all_data = full_data['get_all']
        self.list_by_ids = []
        self.add_object = {}
        self.update_object = {}
        self.delete_object = full_data['delete']
        self._id = 0
        self.name = ''
        self.data = {}

    def get_list_by_ids(self, ids):
        for _id in ids:
            for obj in self.all_data:
                if obj['id'] == str(_id):
                    self.list_by_ids.append(obj)
        return self.list_by_ids

    def get_single_object(self, _id):
        for obj in self.all_data:
            if obj['id'] == str(_id):
                self._id = _id
                self.name = obj['name']
                self.data = obj['data']
                return obj

    def set_add_object(self, obj_type):
        self.add_object = self.full_data[obj_type]
        return self.add_object

    def set_update_object(self, obj_type):
        self.update_object = self.full_data[obj_type]
        return self.update_object

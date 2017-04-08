from loader.api.storage import Storage

class File():

    def __init__(self, id, body):

        if id:
            self.id = id
            self.status = Storage.get_file(id)
            return

        if body:
            self.id, self.status = Storage.add_file(body)
            return

        raise ValueError

    def get_status(self):
        pass
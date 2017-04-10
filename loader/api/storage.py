class Storage(object):

    content = {}
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Storage, cls).__new__(cls)
            cls.__instance.__initialized = False
        return cls.__instance

    def __init__(self):
        if self.__initialized:
            return
        self.__initialized = True

    def add(self, id_file, task):
        if id_file in self.content:
            raise TypeError
        self.content[str(id_file)] = task

    def get_task(self, id_file):
        if str(id_file) not in self.content:
            raise ValueError
        return self.content[str(id_file)]

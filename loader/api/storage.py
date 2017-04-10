from loader.api.file import File
from loader.models import DownloadFile


class Storage(object):

    content = {}
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Storage,cls).__new__(cls)
            cls.__instance.__initialized = False
        return cls.__instance

    def __init__(self):
        if (self.__initialized): return
        self.__initialized = True
        self.initial()

    def add(self, file):
        if file.id in self.content:
            raise TypeError
        self.content[str(file.id)] = file

    def get_file(self, id):
        if str(id) not in self.content:
            raise ValueError
        return self.content[str(id)]

    def initial(self):
        print('init')
        for file in DownloadFile.objects.all():
            self.content[str(file.id)] = File(file.id)

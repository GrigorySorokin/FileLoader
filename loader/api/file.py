from loader.models import DownloadFile


class File:

    percent = 0
    length = -1
    done = False

    def __init__(self, id_file):
        if id_file:
            self.id = id_file
        else:
            raise TypeError
        self.db_instance = DownloadFile.objects.get(id=self.id)
        if self.db_instance.length != -1:
            self.percent = 100
            self.done = True
            self.length = self.db_instance.length

    def set_percent(self, percent):
        if 0 < percent > 100:
            raise ValueError
        self.percent = percent

    def set_result(self, result):
        print(result)
        if result < 0:
            raise ValueError
        self.db_instance.length = result
        self.db_instance.save()
        self.done = True
        self.length = result

    def get_status(self):
        return {
            'percent': self.percent,
            'length': self.length,
            'done': self.done
        }

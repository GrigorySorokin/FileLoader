from django.db import models
import os
# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class DownloadFile(models.Model):

    file = models.FileField()
    length = models.IntegerField()

    def filename(self):
        return os.path.basename(self.file.name)

class ResultTask(models.Model):

    id_file = models.IntegerField()
    percent = models.IntegerField()
    done = models.BooleanField()
    length = models.IntegerField()

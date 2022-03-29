# Create your models here.
from django.db import models

class Tag(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200,default='')

    def __str__(self):
        if self.title !='':
            return f'{self.title}'
        else:
            return ''

class Note(models.Model):
    id = models.BigAutoField(primary_key=True)
    tag = models.ForeignKey(Tag,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=200)
    content = models.TextField(default='')

    def __str__(self):
        return f"{self.id}.{self.title}"

from django.db import models

class Topic(models.Model):
    nom = models.CharField(max_length=150)
    def __str__(self):return self.nom

class Audio(models.Model):
    name = models.CharField(max_length=300)
    fayl = models.FileField()
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name


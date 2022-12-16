from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Task(models.Model):
    tittle =  models.CharField(max_length=200)
    description = models.TextField(max_length=500, blank=False, null=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    done = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField( auto_now_add = True)

    def __str__(self):
        return self.tittle + ' - ' + self.project.name
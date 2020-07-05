from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Course(models.Model):
    code = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    classes = models.IntegerField(default=0)
    classesAttended = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="course", null=True)

    class Meta:
        ordering = ['code']

    def __str__(self):
        return self.code

    @property
    def calculatePercentage(self):
        if(self.classes != 0):
            return "{0:.1f}".format(100*self.classesAttended/(self.classes))+"%"  # noqa
        else:
            return "%"

    @property
    def addAttended(self):
        self.classes += 1
        self.classesAttended += 1
        self.save()

    @property
    def addMissed(self):
        self.classes += 1
        self.save

    @property
    def classesMissed(self):
        return self.classes-self.classesAttended

    @property
    def reset(self):
        self.classes = 0
        self.classesAttended = 0

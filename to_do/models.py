from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.


class toDoItem(models.Model):
    date_create = models.DateField(default=now().date())
    date_due = models.DateField()
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=10000, blank=True)
    category = models.CharField(max_length=100)
    done = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="item", null=True)

    class Meta:
        ordering = ['done', 'date_due', 'category']

    def __str__(self):
        return self.title

    @property
    def markDone(self):
        self.done = True

    @property
    def undo(self):
        self.done = False

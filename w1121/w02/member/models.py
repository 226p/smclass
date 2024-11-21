from django.db import models

class Member(models.Model):
  id = models.CharField(primary_key=True, max_length=50)
  pw = models.CharField(null=False, max_length=100)
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name


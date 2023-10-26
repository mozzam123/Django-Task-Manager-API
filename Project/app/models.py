from djongo import models

# Create your models here.


class User(models.Model):
    _id = models.ObjectIdField()
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    class Meta:
        db_table = "User"
        managed = True

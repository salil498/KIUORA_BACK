from django.db import models



class Data(models.Model):
    name = models.CharField(max_length=250)
    username = models.CharField(max_length=250)
    dob = models.DateField(blank=True)
    gender = models.CharField(max_length=250,blank=True)
    email = models.CharField(max_length=250)
    number = models.BigIntegerField(blank=True)
    password = models.CharField(max_length=250)
    uniq_id = models.AutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'Data'
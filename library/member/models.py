from django.db import models

# Create your models here.

class Member(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField()
    username = models.CharField(max_length = 12, blank = True, null = True)
    password = models.CharField(max_length=15, blank = True, null = True)
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        db_table = 'member'

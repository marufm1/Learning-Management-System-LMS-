from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')
    faculty_description = models.TextField()
    designation = models.CharField(max_length = 250)
    office = models.CharField(max_length = 250)
    phone = models.CharField(max_length = 250)
    website = models.CharField(max_length = 250)



    def __str__(self):
        return f'{self.user.username} Profile'

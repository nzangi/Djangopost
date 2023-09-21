from django.db import models
from PIL import Image
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.png',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile' #model yake
    
    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300or img.width >200:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)



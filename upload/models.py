from django.db import models
from django.contrib.auth.models import User
import choices 

class upload(models.Model):
    get_file=models.FileField(upload_to="site_media/uploads/",null=False,blank=False)
    uploaded_by=models.ForeignKey(User)
    uploaded_for=models.CharField(max_length=30,blank=True,null=True)
    access_level=models.SmallIntegerField(blank=False)

    class Meta:
        db_table="uploads"

class image(models.Model):
    '''Handles the uplaoad of images for a more cmssy feel
    I intend to make the images accesible by templates via
    a dictionary passed containing all locations'''
    file = models.ImageField( upload_to = "site_media/im/" )
    
    def __unicode__(self):
        return self.file

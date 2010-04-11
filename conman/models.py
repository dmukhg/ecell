from django.db import models

class Images(models.Model):
    '''A table of all the images the organisation has'''
    file=models.ImageField(upload_to="/site_media/images/upload")
    date = models.DateTimeField()
  
    def __unicode__(self):
        return self.file;

    class Meta:
        db_table="images"


#the first three form the part of featured content
class Video (models.Model):
    '''A table of all the featured video that has ever been put up on the site'''
    title=models.CharField(max_length=250,unique=True)#title-must be unique
    url=models.URLField(verify_exists=True,unique=True)#the url of the video, this field must be unique
    description=models.CharField(max_length=1024)#a short description of what the video is about
    date = models.DateTimeField()

    def __unicode__(self):
        return self.title

    class Meta:
        db_table="featured_video"
    

class Startup (models.Model):
    '''A table of all the startups that has been featured'''
    title=models.CharField(max_length=250,unique=True)#title-must be unique
    profile=models.TextField()#the profile of the startup
    image=models.OneToOneField(Images)#an associated image of the startup
    date = models.DateTimeField()

    def __unicode__(self):
        return self.title

    class Meta:
        db_table="featured_startup"

class Entrepreneur (models.Model):
    '''A table of all the Entrepreneurs that habe been featured'''
    name=models.CharField(max_length=250,unique=True)#name-must be unique
    profile=models.TextField()#the profile of the entrepreneur
    image=models.OneToOneField(Images)#an associated image of the startup
    date = models.DateTimeField()

    def __unicode__(self):
        return self.name

    class Meta:
        db_table="featured_entrepreneur"

class Article(models.Model):
    content = models.TextField()
    frontpage = models.BooleanField(default = False)
    date = models.DateField()
    

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = "article"

class Sector(models.Model):
    '''A collection of all categories to be reported in the top nav bar to implement a hierarchy of sorts'''
    name = models.CharField(max_length = 50 , unique = True)
    display_order = models.SmallIntegerField()
    url = models.CharField(max_length = 50 , unique = True)
    article = models.ForeignKey(Article,null=True)
    image = models.OneToOneField(Images,null=True)
    parent = models.ForeignKey("self",null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table="sector"


class Updates(models.Model):
    '''A collection of all updates the site has seen till date. The chronologically recent updates will show on the home page.'''
    # short description to be shown as tab on the updates panel
    description = models.CharField(max_length = 100)
    # longer description of the update to be shown on the panel
    content = models.CharField(max_length = 400)
    # this will be the order of display
    date = models.DateField()
    image = models.ForeignKey(Images,null=True)
    # since an update need not correspond to a sector, we hard link it to an article with a different url scheme
    # such as updates/foo or updates/bar
    url = models.CharField(max_length = 50, null = True)
    # for such articles the articles to which they correspond must also be hardlinked so..
    article = models.ForeignKey(Article, null = True)

    class Meta:
        db_table = "updates"

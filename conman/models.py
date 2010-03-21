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

class Resources(models.Model):
    '''A table of all the informative resources posessed by the organisation'''
    file=models.FileField(upload_to="/site_media/content")
    date = models.DateTimeField()

    def __unicode__(self):
        return self.name;

    class Meta:
        db_table="resources" 
	
class Section(models.Model):
	'''A collection of all categories to be reported in the top nav bar'''
	name = models.CharField(max_length = 50 , unique = True)
	url = models.CharField(max_length = 50 , unique = True)
	order = models.SmallIntegerField(unique = True)
	image = models.OneToOneField(Images,null=True)
#	ddfollowers = models.ManyToManyField(
	
	def __unicode__(self):
		return self.name

	class Meta:
		pass

class Article(models.Model):
	'''An article'''
	title = models.SlugField()
	url = models.CharField(max_length=100)
        content = models.TextField()
	section = models.ForeignKey(Section)
	frontpage = models.BooleanField()
	date = models.DateField()

	def __unicode__(self):
		return self.title

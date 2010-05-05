from django.db import models
from ecell2.upload.models import image

class Article(models.Model):
    content = models.TextField()
    frontpage = models.BooleanField(default = False)
    date = models.DateField()
    

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = "article"

class Sector(models.Model):
    '''A collection of all categories to be reported in the top
    nav bar to implement a hierarchy of sorts'''
    name = models.CharField(max_length = 50 , unique = True)
    display_order = models.SmallIntegerField()
    url = models.CharField(max_length = 50 , unique = True)
    article = models.ForeignKey(Article,null=True)
    image = models.OneToOneField(image,null=True)
    parent = models.ForeignKey("self",null=True)

    def __unicode__(self):
        return self.name

    def get_url(self):
        up = self
        rendered_url = self.url 
        while up.parent is not None:
            rendered_url = up.parent.url + '/' + rendered_url
            up = up.parent
        rendered_url = u'/' + rendered_url
        return rendered_url


    class Meta:
        db_table="sector"


class Updates(models.Model):
    '''A collection of all updates the site has seen till date.
    The chronologically recent updates will show on the home page.'''
    # short description to be shown as tab on the updates panel
    description = models.CharField(max_length = 100)
    # longer description of the update to be shown on the panel
    content = models.CharField(max_length = 400)
    # this will be the order of display
    date = models.DateField()
    image = models.ForeignKey(image,null=True)
    # since an update need not correspond to a sector, we hard link it to an article with a different url scheme
    # such as updates/foo or updates/bar
    url = models.CharField(max_length = 50, null = True)
    # for such articles the articles to which they correspond must also be hardlinked so..
    article = models.ForeignKey(Article, null = True)

    class Meta:
        db_table = "updates"

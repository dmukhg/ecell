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
    display_order = models.SmallIntegerField( default = 0)
    url = models.CharField(max_length = 50 , unique = True)
    article = models.ForeignKey(Article,null=True)
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
    
    description = models.CharField(max_length = 100)    # short description to be shown as tab on the updates panel
    content = models.CharField(max_length = 400)        # longer description of the update to be shown on the panel
    date = models.DateField()                           # this will be the order of display
    url = models.CharField(max_length = 50, null = False)# url the update refers to
    active = models.BooleanField( default = True )

    class Meta:
        db_table = "updates"

    def __unicode__(self):
        return u'<Update: \' ' + self.description + '\' > '


class Snippets( models.Model ):
    '''The home page/s should be made of snippets from various sub cateories.
    Required features:
        > Editable
        > Linked
        > Imaged
    '''
    image_filename = models.CharField( max_length = 100 )
    content = models.CharField( max_length = 400 )
    url = models.CharField( max_length = 50 , null = True )

    class Meta:
        db_table = 'snippets'

    def __unicode__( self ):
        return u'<Snippet: \' ' + self.image_filename.split('.')[0] + '\' >'


class Page(models.Model):
    '''
    This model represents all such pages that have no clear parentage in 
    the site hierarchy. Urls will be of the form
        domain.com/pages/whatever-it-is-that-we-are-referring-to
    To enable UTF content with ASCII URLs, title will be separate from the
    url.
    '''
    title = models.CharField( max_length=200 )
    url = models.CharField( max_length=200 )
    content = models.TextField()

    class Meta:
        db_table = 'pages'
    
    def __unicode__( self ):
        return u'<Page: \' ' + self.url + '\' >'


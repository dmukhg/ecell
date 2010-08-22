from django.db import models
from django.contrib.auth.models import User
from ecell2.conman.core.models import *
import ecell2.account.choices as choices


# Create your models here.
class person(models.Model):
     ''' defines all the attributes that defines a person. inherits from user. this class further forms the base class of other types of users'''
     user_ptr=models.ForeignKey(User)
     sex=models.CharField(max_length=1,choices=choices.sex_choice,blank=False)#internally corresponds to character choice of m or f
     occupation=models.CharField(max_length=10,choices=choices.occupation_choice)#a choice of occupation which internally corresponds to a number
     phno=models.CharField(max_length=15,verbose_name='phone-number')#phone number of the user
     institution=models.CharField(max_length=100)
     address=models.CharField(max_length=250)
     pin=models.CharField(max_length=10)
     website=models.URLField(verify_exists=True,null=True,blank=True)#url of the website of the user
#     follows=models.ManyToManyField(Article)

     def __unicode__(self):
	             return "%s %s %s" % (self.first_name, self.last_name, self.institution) 

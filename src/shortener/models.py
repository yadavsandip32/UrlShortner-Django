from django.db import models

from .utils import code_generator

class KirrURL(models.Model):
    url = models.CharField(max_length=200)
    shorturl = models.CharField(max_length=20,unique=True, null=False,blank=True)
    updated = models.DateTimeField(auto_now=True) #Everytime model is saved
    timestamp = models.DateTimeField(auto_now_add=True) #when model was created
    #
    # # shorturl = models.CharField(max_length=20)
    # # shorturl = models.CharField(max_length=20)
    #

    def save(self, *args, **kwargs):
        if self.shorturl is None or self.shorturl == "":
            self.shorturl = code_generator()
        super(KirrURL,self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)

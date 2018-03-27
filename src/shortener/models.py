from django.db import models

from .utils import code_generator, createshorturl

class KirrUrlManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(KirrUrlManager,self).all(*args,**kwargs)
        qs = qs_main.filter(Active=False)
        return qs

    def refresh_url(self):
        new_url =0
        qs = KirrURL.objects.filter(id__gte=1)
        for q in qs:
            q.shorturl = createshorturl(q)
            print(q.shorturl)
            q.save()
            new_url += 1
        return "New urls made: {i}".format(i=new_url)


class KirrURL(models.Model):
    url        = models.CharField(max_length=200)
    shorturl   = models.CharField(max_length=20,unique=True, null=False,blank=True)
    updated    = models.DateTimeField(auto_now=True) #Everytime model is saved
    timestamp  = models.DateTimeField(auto_now_add=True) #when model was created
    Active     = models.BooleanField(default=True)

    objects = KirrUrlManager()

    def save(self, *args, **kwargs):
        if self.shorturl is None or self.shorturl == "":
            self.shorturl = code_generator()
        super(KirrURL,self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)

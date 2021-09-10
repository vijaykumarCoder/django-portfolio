from django.db import models
from django.db.models.signals import post_save, pre_save
from django.utils.text import slugify

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    headline= models.CharField(max_length=100)
    subHeadline =  models.CharField(max_length=200,null=True, blank=True)
    thumnails = models.ImageField(null=True,blank=True)
    body= models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    featured= models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, null=True)
    #slug = models.SlugField(unique=True)
 
    def __str__(self):
        return self.headline

class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="static/images", null=True)

    def __str__(self):
        return self.title

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=True,blank=True)

def create_slug(instance,new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    
    qs = BlogPost.objects.filter(slug = slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, instance.id)
        return create_slug(instance, new_slug=new_slug)
    return slug

    


def BlogPost_slug(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
pre_save.connect(BlogPost_slug, sender=BlogPost)
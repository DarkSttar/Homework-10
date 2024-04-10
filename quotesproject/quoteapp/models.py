from django.db import models

class Tag(models.Model):
    tag = models.CharField(max_length=100,null=False)

class Author(models.Model):
    name = models.CharField(max_length=50, null=False)
    born_date = models.CharField(max_length=50,null=False)
    born_location = models.CharField(max_length=150, null=False)
    description = models.TextField(null=False)

    def __str__(self):
        return self.name
class Quote(models.Model):
    quote = models.TextField(null=False)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,default=None,null=True)
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return self.quote

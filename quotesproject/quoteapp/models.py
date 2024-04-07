from django.db import models

class Tag(models.Model):
    tag = models.CharField(max_length=20,null=False)

class Author(models.Model):
    name = models.CharField(max_length=50, null=False)
    born_date = models.DateTimeField('Born_date')
    born_location = models.CharField(max_length=150, null=False)
    description = models.CharField(max_length=3000,null=False)

    def __str__(self):
        return self.name
class Quote(models.Model):
    quote = models.CharField(max_length=1000, null=False)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    def __str__(self):
        return self.quote

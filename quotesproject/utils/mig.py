import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quotesproject.settings")
django.setup()



from quoteapp.models import Quote,Tag,Author

from pymongo import MongoClient

client = MongoClient("mongodb+srv://DarkStar:Dark10101994@clusterdsk.2ofj9mx.mongodb.net/?retryWrites=true&w=majority&appName=ClusterDSK")

db = client.AuthorsDB

authors = db.author.find()

for author in authors:
    Author.objects.get_or_create(
        name=author['fullname'],
        born_date=author['born_date'],
        born_location=author['born_location'],
        description=author['description']
    )


quotes = db.quote.find()


for quote in quotes:
    tags = []
    for tag in quote['tags']:
        t, *_ = Tag.objects.get_or_create(tag=tag)
        tags.append(t)

    exist_quote  = bool(len(Quote.objects.filter(quote=quote['quote'])))

    if not exist_quote:
        author = db.author.find_one({'_id':quote['author']})
        a = Author.objects.get(name=author['fullname'])
        q = Quote.objects.create(
            quote=quote['quote'],
            author=a
        )
        for tag in tags:
            q.tags.add(tag)
from django.shortcuts import render ,redirect
from .forms import QuotesForm,TagForm,AuthorForm
from .models import Author,Quote,Tag
def main(request):
    quotes = Quote.objects.all()
    return render(request,'quoteapp/index.html',{'quotes':quotes})



def addquote(request):
    tags = Tag.objects.all()
    author = Author.objects.all()
    
    
    if request.method == 'POST':
        form = QuotesForm(request.POST)
        if form.is_valid():
            new_quote = form.save()
            choice_tags = Tag.objects.filter(tag__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                new_quote.tags.add(tag)
            return redirect('quoteapp:main')  
    
    return render(request, 'quoteapp/addquote.html', {'tags':tags, 'author': author, 'form': QuotesForm()})
def addtag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quoteapp:main')
    else:
        form = TagForm()
    return render(request,'quoteapp/addtag.html',{'form':form})

def addauthor(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quoteapp:main')
    else:
        form = AuthorForm()
        return render(request,'quoteapp/addauthor.html',{'form':form})
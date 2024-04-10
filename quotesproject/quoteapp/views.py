from django.shortcuts import render ,redirect, get_object_or_404
from .forms import QuotesForm,TagForm,AuthorForm
from .models import Author,Quote,Tag
from django.core.paginator import Paginator

def quotes_by_tag(request,tag_id):
    tag = get_object_or_404(Tag,pk=tag_id)

    quotes = Quote.objects.filter(tags=tag)

    return render(request,'quoteapp/index.html', {'quotes':quotes})

def author_detail(request,author_id):
    author = Author.objects.get(pk=author_id)
    return render(request,'quoteapp/author_detail.html',{'author':author})

def main(request, page=1):
    top_tags = {}
    quotes = Quote.objects.all()
        

    per_page = 10
    paginator = Paginator(list(quotes),per_page=per_page)
    quotes_on_page = paginator.page(page)
    
    

    return render(request,'quoteapp/index.html',{'quotes':quotes_on_page})



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
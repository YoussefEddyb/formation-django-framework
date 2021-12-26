from django.shortcuts import redirect, render
from .forms import ArticleForm
from .models import Article


# Create your views here.
def index(request):
    return render(request, "index.html", {
        "articles": Article.objects.filter(state=1)
    })

def show(request, id):
    return render(request, "show.html", {
        "article": Article.objects.get(pk=id)
    })

def create(request):
    form  = ArticleForm
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_of_articles')
    return render(request, "create.html", {
        "form": form
    })

def edit(request, id):
    article = Article.objects.get(pk=id)
    form = ArticleForm(instance=article)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('list_of_articles')
    return render(request, "edit.html", {
        'form': form
    })

def delete(request, id):
    article = Article.objects.get(pk=id)
    if request.method == 'POST' :
        article.delete()
        return redirect('list_of_articles')
    

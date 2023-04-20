from django.shortcuts import render, redirect
from . models import Articles
from . forms import ArticleFrom
from django.views.generic import DetailView, UpdateView, DeleteView
# Create your views here.




def news_home(request):
    news = Articles.objects.all().order_by('-title')
    return render(request, 'newsp/news_home.html', {'news': news}) # can also ... 'mainp/aboutus.html'


class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'newsp/news-delete.html'


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'newsp/add_form.html'
    
    form_class = ArticleFrom


class NewsDetailView(DetailView):  ## check ListView
    model = Articles
    template_name = 'newsp/detail_view.html'
    context_object_name = 'article'


def add_article(request):
    error = ''
    if request.method == 'POST':
        form = ArticleFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = "Invalid input!"

    form = ArticleFrom()
    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'newsp/add_form.html', data)
from http.client import HTTPResponse
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from articles.models import Article
from django.template.loader import render_to_string
from random import randint
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
# Create your views here.


def article_home_view(request):
    return HttpResponse()

def home_view(request, *args, **kwargs):
    random_id = randint(1, 2)
    article_obj = Article.objects.get(id=random_id)
    article_queryset = Article.objects.all()

    context = {
        "object_list":article_queryset,
        "object":article_obj,
        "title":article_obj.title,
        "content":article_obj.content
    }

    HTML_STRING = render_to_string("home-view.html", context=context)

    # HTML_STRING = """
    # <h1>{title}</h1>

    # <p>{content}</p>
    # """.format(**context)
    
    return HttpResponse(HTML_STRING)

def article_detail_view(request, slug=None):
    article_obj=None
    if slug is not None:
        try:
            article_obj = Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise Http404
        except:
            raise Http404

    context = {
        # "object_list":article_queryset,
        "object":article_obj,
        "title":article_obj.title,
        "content":article_obj.content
    }

    return render(request, "articles/detail.html", context)

@login_required
def article_create_view(request, id=None):
    form = ArticleForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        article_object = form.save()
        context['form'] = ArticleForm()
        return redirect(article_object.get_absolute_url())
        # context['object'] = article_object
        # context['created'] = True

    return render(request, "articles/create.html", context=context)


def article_search_view(request):

    query = request.GET.get('q')
    qs = Article.objects.search(query=query)
    context = {
        "object_list":qs
    }

    return render(request, "articles/search.html", context=context)
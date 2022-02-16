from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render
from articles.models import Article
from django.template.loader import render_to_string
from random import randint
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
# Create your views here.


def article_home_view(request):
    return HttpResponse()

def article_search_view(request):

    query_dict = request.GET
    # query = query_dict.get("q")

    try:
        query = int(query_dict.get("q"))
    except:
        query = None

    article_obj = None
    if query is not None:
        article_obj = Article.objects.get(id=query)
    context = {
        "object":article_obj
    }

    return render(request, "articles/search.html", context=context)


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

def article_detail_view(request, id=None):
    article_obj=None
    if id is not None:
        article_obj = Article.objects.get(id=id)

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
        # context['object'] = article_object
        # context['created'] = True

    return render(request, "articles/create.html", context=context)
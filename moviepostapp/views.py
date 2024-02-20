
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import MovieForm
from .models import Category,Movie
from django.core.paginator import Paginator,EmptyPage,InvalidPage

from moviepostapp.models import Movie




# Create your views here.


def allMovieCat(request,c_id=None):
    c_page=None
    movies_list=None
    if c_id!=None:
        c_page=get_object_or_404(Category,id=c_id)
        movies_list=Movie.objects.all().filter(category=c_page)
    else:
        movies_list=Movie.objects.all()
    paginator=Paginator(movies_list,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        movies=paginator.page(page)
    except (EmptyPage,InvalidPage):
        movies=paginator.page(paginator.num_pages)

    return render(request,"category.html",{'category':c_page,'movies':movies})

def movieDetail(request,c_id,movie_id):
    try:
        movie = Movie.objects.get(category__id=c_id, id=movie_id)
    #
    except Exception as e:
        raise e
    except Movie.DoesNotExist:
         movie = get_object_or_404(Movie, category__id=c_id, id=movie_id)

    return render(request,"movie.html",{'movie':movie})



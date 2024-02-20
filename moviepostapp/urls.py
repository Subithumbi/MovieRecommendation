from django.urls import path, include

from .import views

app_name='moviepostapp'

urlpatterns = [
    path('', views.allMovieCat, name='allMovieCat'),
    path('<int:c_id>/', views.allMovieCat, name='movies_by_category'),
    path('<int:c_id>/<str:movie_id>/', views.movieDetail, name='movieCatdetail'),

]
from django.urls import path
from .import views
app_name='movieapp'

urlpatterns=[
    path('',views.movie_list,name='movie_list'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('movies/<int:movie_id>/',views.details,name='details'),
    path('add/',views.add_movie,name='add_movie'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
]
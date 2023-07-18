from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import MovieForm
from .models import Movie
# Create your views here.
def movie_list(request):
    movie=Movie.objects.all()
    context={'movie_list':movie}
    return render(request,"movie_list.html",context)

def detail(request,movie_id):
    return HttpResponse("This is movie number %s" % movie_id)

def details(request,movie_id):
    detail=Movie.objects.get(id=movie_id)
    return render(request,"details.html",{'detail':detail})

def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name')
        category = request.POST.get('category')
        director = request.POST.get('director')
        year = request.POST.get('year')
        img = request.FILES['img']

        movie=Movie(name=name,category=category,director=director,year=year,img=img)
        movie.save()
        return redirect('/')
    return render(request,"add_movie.html")

def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"update.html",{'form':form,'movie':movie})

def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,"delete.html")
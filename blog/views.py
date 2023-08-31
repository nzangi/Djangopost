from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author':'Nzangi Muoki',
        'title' : 'Blog Post 1',
        'content' : 'Soccer new for today',
        'date' : '31 August, 2023'
    },
    {
        'author':'Munyoki Muoki',
        'title' : 'Blog Post 3',
        'content' : 'Cricket new for today',
        'date' : '29 August, 2023'
    },
    {
        'author':'Neema Muoki',
        'title' : 'Blog Post 3',
        'content' : 'Footaball news for today',
        'date' : '30 August, 2023'
    }
]
def home(request):
    context = {
        'posts' : posts
    }
    home={'title': 'Home Page'}
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html',{'title': 'About Page'})

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .forms import *
from .models import *

menu =[{'title': "О сайте", 'url_name': 'about'},
       {'title': "Добавить статью", 'url_name': 'add_page'},
       {'title': "Контакты", 'url_name': 'contact'},
       {'title': "Вход", 'url_name': 'login'}]


class MensHome(ListView):
    model = Mens
    template_name = 'mens/index.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Mens.objects.filter(is_published=True)


def about(request):
    return render(request, 'mens/about.html', {'menu': menu})


def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = AddPostForm()

    return render(request, 'mens/addpage.html', {'form' : form, 'menu': menu, 'title' : 'Добавление статьи'})

def contact(request):
    return HttpResponse("Контактная информация")

def login(request):
    return HttpResponse("Авторизация")

def show_post(request, post_slug):
    post = get_object_or_404(Mens, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }
    return render(request, 'mens/post.html', context=context)


def show_category(request, cat_id):
    posts = Mens.objects.filter(cat_id=cat_id)

    context = {
        'post': posts,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_celected': cat_id,
    }
    return render(request, 'mens/index.html', context=context)

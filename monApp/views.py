from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import RegisterForm, LoginForm

# Create your views here.


def home(request):
    return render(request, 'home.html')

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'Blog/article_list.html', {'articles': articles})


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'Blog/article_detail.html', {'article': article})


def profile(request):
    return render(request, 'Users/profile.html')

def login(request):
    return render(request, 'Users/login.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('profile')
    else:
        form = RegisterForm()
    return render(request, 'Users/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = LoginForm()
    return render(request, 'Users/login.html', {'form': form})
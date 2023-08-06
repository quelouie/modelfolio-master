from django.shortcuts import render
from .models import Project, About
from .forms import ContactForm

projectsList = [{
    'id': '1',
    'picture': 'picture 1',
    'title': 'title',
    'description' : "description of the picture"
    },{
    'id': '2',
    'picture': 'picture 2',
    'title': 'title',
    'description' : "description of the picture"
    },{
    'id': '3',
    'picture': 'picture 3',
    'title': 'title',
    'description' : "description of the picture"
    }
]

def home(request):
    page = 'home'
    context = {'page': page}
    return render(request, 'home.html', context)

def about(request):
    page = 'about'
    about = About.objects.all()
    context = {'page': page, 'about': about}
    return render(request, 'projects/about.html', context)

def projects(request):
    page = 'album'
    projects = Project.objects.all()
    context = {'page': page, 'projects': projects}
    return render(request, 'projects/projects.html', context)

def contact(request):
    page = 'about'
    about = About.objects.all()
    context = {'page': page, 'about': about}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'projects/about.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'projects/contact.html', context)

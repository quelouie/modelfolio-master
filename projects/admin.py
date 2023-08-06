from django.contrib import admin

# Register your models here.
from .models import Project, About, Contact

admin.site.register(Project)
admin.site.register(About)
admin.site.register(Contact)
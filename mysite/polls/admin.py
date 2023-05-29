from django.contrib import admin

# Register your models here.

from polls.models import Author, Presentation

admin.site.register(Author)
admin.site.register(Presentation)
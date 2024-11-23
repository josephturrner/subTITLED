from django.contrib import admin
from .models import YTMedia, DifficultWord, IncorrectWord

# Register your models here.
admin.site.register(YTMedia)
admin.site.register(DifficultWord)
admin.site.register(IncorrectWord)
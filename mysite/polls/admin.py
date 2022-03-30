from django.contrib import admin

# Register your models here.

# need to tell admin which obejcts have admin interface
from .models import Question, Choice
admin.site.register(Question)
admin.site.register(Choice)

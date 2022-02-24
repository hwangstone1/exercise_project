from django.contrib import admin
from .models import Question
# Register your models here.

class QusetionAdmin(admin.ModelAdmin):
    search_fields = ['subject','content']

admin.site.register(Question,QusetionAdmin)

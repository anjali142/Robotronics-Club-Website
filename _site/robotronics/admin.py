from django.contrib import admin

from .models import Member, Project, Tutorial

admin.site.register(Member)
admin.site.register(Project)
admin.site.register(Tutorial)

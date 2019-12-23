from django.contrib.admin import site, ModelAdmin
from voteapp.models import *
from django.contrib import admin

admin.site.register(Voting)
admin.site.register(Menu)
admin.site.register(Restaurant)

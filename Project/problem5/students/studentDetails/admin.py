from django.contrib import admin

# Register your models here.
from .models import Insert, Search

admin.site.register(Insert)
admin.site.register(Search)

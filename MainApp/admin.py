from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(History)
admin.site.register(SiteSettings)
admin.site.register(NewsAndEvents)

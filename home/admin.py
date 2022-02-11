from django.contrib import admin
from .models import DateRel, Artist, AboutInfo, Attraction

# Register your models here.

admin.site.register(Artist)
admin.site.register(AboutInfo)
admin.site.register(Attraction)
admin.site.register(DateRel)

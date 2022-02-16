from django.contrib import admin
from .models import (
    DateRel,
    Artist,
    AboutInfo,
    Attraction,
    Sponsor,
    FrontImage,
    FrontHeading,
    NavbarHeading,
)

# Register your models here.

admin.site.register(NavbarHeading)
admin.site.register(FrontHeading)
admin.site.register(FrontImage)
admin.site.register(AboutInfo)
admin.site.register(Artist)
admin.site.register(Attraction)
admin.site.register(Sponsor)
admin.site.register(DateRel)

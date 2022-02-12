from django.contrib import admin
from .models import DateRel, Artist, AboutInfo, Attraction, Sponsor, SponsorImage

# Register your models here.


class SponsorImageAdmin(admin.StackedInline):
    model = SponsorImage


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    inlines = [SponsorImageAdmin]

    class Meta:
        model = Sponsor


@admin.register(SponsorImage)
class SponsorImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Artist)
admin.site.register(AboutInfo)
admin.site.register(Attraction)
admin.site.register(DateRel)

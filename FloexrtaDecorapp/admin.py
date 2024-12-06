from django.contrib import admin
from .models import User, Bookings, ImageModel, NavigationLink,contactinfo

class NavigationLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_url')  


admin.site.register(NavigationLink, NavigationLinkAdmin)
admin.site.register(User)
admin.site.register(Bookings)
admin.site.register(ImageModel)
admin.site.register(contactinfo)


from django.contrib import admin
from .models import User, Bookings, ImageModel, NavigationLink  # Import models once

class NavigationLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_url')  # Show title and clickable URL in the list view

# Register models
admin.site.register(NavigationLink, NavigationLinkAdmin)
admin.site.register(User)
admin.site.register(Bookings)
admin.site.register(ImageModel)

from django.contrib import admin

# Register your models here.
from website.models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    # Optional: Customize the list of displayed fields
    list_display = ['name', 'email']

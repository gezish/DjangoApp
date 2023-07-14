from django.contrib import admin

# Register your models here.
from . import models
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title',)
    
class ContactsAdmin(admin.ModelAdmin):
    Contacts_display = ('contact_name', )

admin.site.register(models.Notes, NoteAdmin)
admin.site.register(models.Contacts, ContactsAdmin)
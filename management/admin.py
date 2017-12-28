from django.contrib import admin
from management.models import Characters


class CharactersAdmin(admin.ModelAdmin):
    using = 'l2server'
    def get_queryset(self, request):
        # Tell Django to look for objects on the 'other' database.
        return super(CharactersAdmin, self).get_queryset(request).using(self.using)
# Register your models here.


admin.site.register(Characters, CharactersAdmin)

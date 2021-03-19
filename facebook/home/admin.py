from django.contrib import admin

# Register your models here.
from .models import Person,Contact,User
admin.site.register(Person)
admin.site.register(Contact)
admin.site.register(User)

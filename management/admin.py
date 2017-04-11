from django.contrib import admin
from .models import MyUser,Book,Img

# Register your models here.
admin.site.register(MyUser)
admin.site.register(Img)
admin.site.register(Book)
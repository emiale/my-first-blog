from django.contrib import admin
from .models import Post

# Register your models here.

#registranuestro objeto post en el administrador de Django para 
#poder consultar o actualiza informacion del o de los Post's
admin.site.register(Post)
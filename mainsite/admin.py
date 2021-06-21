from django.contrib import admin
from .models import Post, Visitor_202105, Visitor_202104, Visitor_202103, Visitor_202102, Visitor_202101

#####
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'pub_date')
admin.site.register(Post, PostAdmin)

class Visitor_202105Admin(admin.ModelAdmin):
    list_display = ('date', 'number')
admin.site.register(Visitor_202105,Visitor_202105Admin)

class Visitor_202104Admin(admin.ModelAdmin):
    list_display = ('date', 'number')
admin.site.register(Visitor_202104,Visitor_202104Admin)

class Visitor_202103Admin(admin.ModelAdmin):
    list_display = ('date', 'number')
admin.site.register(Visitor_202103,Visitor_202103Admin)

class Visitor_202102Admin(admin.ModelAdmin):
    list_display = ('date', 'number')
admin.site.register(Visitor_202102,Visitor_202102Admin)

class Visitor_202101Admin(admin.ModelAdmin):
    list_display = ('date', 'number')
admin.site.register(Visitor_202101,Visitor_202101Admin)
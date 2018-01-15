from django.contrib import admin
from TestModel import models
from TestModel.models import Test,Contact,Tag
'''
class TestAdmin(admin.ModelAdmin):
    list_display = ('name','')

class TagAdmin(admin.ModelAdmin):
    list_display = ('name','')
'''
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','age','email')
    search_fields = ('age',)
    list_filter = ('name',)

admin.site.register(Test)
admin.site.register(Tag)
admin.site.register(Contact,ContactAdmin)



# Register your models here.

from django.contrib import admin
from testApp.models import *

# Register your models here.
class hydjobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phoneno']


class bangjobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phoneno']

class punejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phoneno']

class indorejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phoneno']

admin.site.register(hydjobs,hydjobsAdmin)
admin.site.register(punejobs,punejobsAdmin)
admin.site.register(bangjobs,bangjobsAdmin)
admin.site.register(indorejobs,indorejobsAdmin)

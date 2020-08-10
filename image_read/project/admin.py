from django.contrib import admin
from .models import image_extract
# Register your models here.

class image_extractAdmin(admin.ModelAdmin):
    list_display = ('seat_no','image','name','mother_name','college_name','center_no','total_marks')
    list_filter = ['seat_no','image']
    pass

admin.site.register(image_extract,image_extractAdmin)
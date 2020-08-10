from django.views.generic import ListView,DetailView,CreateView
from . import models
from .utils.extract import ext
class ImagelListView(ListView):
    context_object_name = 'Image_Extract'
    template_name = "project/index.html"
    model = models.image_extract

class ImageDetailView(DetailView):
    context_object_name = 'image_detail'
    model = models.image_extract
    template_name = "project/image_detail.html"

    def get_queryset(self):
        return models.image_extract.objects.all()

# class ImageDetailView(DetailView):
#     context_object_name = 'image_detail'
#     model = models.image_extract
#     template_name = "project/image_detail.html"
#
#     def get_queryset(self):
#         pic = models.image_extract.objects.all().values('name')
#         seat = models.image_extract.objects.all().values('seat_no')
#         if pic:
#             # pic_data = pytesseract.image_to_string(Image.open(pic))
#             return pic
#         else:
#             return seat

class ImageCreateView(CreateView):
    fields = ("seat_no","image")
    model = models.image_extract
    template_name = "project/image_upload.html"
    # extrated_data = ext(models.image_extract)

    def __init__(self):
        data = self.model.image
        self.extrated_data = ext(data)
        self.model.save()
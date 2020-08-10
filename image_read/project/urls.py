from django.conf.urls import url
from project import views

# from django.conf import  settings
# from django.conf.urls.static import static

app_name = "project"

urlpatterns = [
    url(r'list',views.ImagelListView.as_view(),name="image"),
    url(r'(?P<pk>\d+)/$', views.ImageDetailView.as_view(), name="image_detail"),
    url(r'create/',views.ImageCreateView.as_view(),name = "create")
    # url(r'^image/(?P<pk>\d+)/$',views.click_image,name= 'image')

]
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
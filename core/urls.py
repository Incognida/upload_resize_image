from django.urls import path
from .views import home, model_form_upload, resize_image

urlpatterns = [
    path('', home, name='home'),
    path('upload/', model_form_upload, name='model_form_upload'),
    path('resize/<str:fname>/', resize_image, name='resize_image'),
]

from django.urls import path
from .views import home, model_form_upload, resize_image

urlpatterns = [
    path('', home, name='home'),
    path('upload/', model_form_upload, name='upload'),
    path('<str:fname>/', resize_image, name='resize'),
]

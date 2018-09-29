import requests
from urllib.parse import urlparse
from django import forms
from django.core.exceptions import ValidationError
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

from .models import Picture
from .utils import check_image_extension


class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ('image',)
    url = forms.URLField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        cleaned_img = cleaned_data.get('image')
        cleaned_url = cleaned_data.get('url')
        picture = Picture()
        if not (cleaned_img or cleaned_url):
            raise ValidationError("There is no image")
        elif not cleaned_img and cleaned_url:
            name = urlparse(cleaned_url).path.split('/')[-1]
            check_image_extension(name)
            content = requests.get(cleaned_url).content
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(content)

            img_temp.flush()

            picture.image.save(name, File(img_temp), save=True)
        else:
            name = cleaned_img.name
            check_image_extension(name)
            picture.image.save(name, File(cleaned_img), save=True)


class ResizeForm(forms.Form):
    size = forms.IntegerField(min_value=1, required=False)
    width = forms.IntegerField(min_value=1, required=False)
    height = forms.IntegerField(min_value=1, required=False)

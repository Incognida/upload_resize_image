from django.shortcuts import render, redirect
from django.conf import settings
from django.views.decorators.http import require_http_methods

from .models import Picture
from .forms import PictureForm, ResizeForm
from .utils import resize


def home(request):
    pictures = Picture.objects.all()
    return render(request, 'core/home.html', {'pictures': pictures})


def model_form_upload(request):
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            return redirect('home')
    else:
        form = PictureForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })


@require_http_methods(["GET", "POST"])
def resize_image(request, fname):
    template_name = 'core/resized_image.html'

    if request.method == 'POST':
        form = ResizeForm(request.POST)
        if form.is_valid():
            size = form.cleaned_data.get('size')
            width = form.cleaned_data.get('width')
            height = form.cleaned_data.get('height')
        else:
            errors = form.errors
            return render(request, template_name, {'errors': errors})
    else:
        size = request.GET.get('size')
        width = request.GET.get('width')
        height = request.GET.get('height')
        form = ResizeForm()

    picture = Picture.objects.filter(image=fname).first()
    errors = resize(picture, width, height, size)

    if width or height:
        picture_url = settings.MEDIA_URL + 'resized_' + picture.image.name
    else:
        picture_url = picture.image.url

    if errors:
        return render(request, template_name, {'errors': errors.values(), 'form': form})
    return render(request, template_name, {'picture_url': picture_url, 'form': form})

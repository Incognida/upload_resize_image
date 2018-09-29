import os
from os.path import splitext

from PIL import Image
from django.core.exceptions import ValidationError


def resize(picture, width=None, height=None, size=None):
    if not picture:
        return {'error': 'there is no such image'}

    pf = picture.image.path
    img = Image.open(pf)

    if not (width or height):
        return None
    elif not width:
        width = img.width
    elif not height:
        height = img.height

    img = img.resize((width, height), Image.ANTIALIAS)

    splitted = pf.rsplit('/', maxsplit=1)
    splitted[-2] += '/resized_'
    new_pf = ''.join(splitted)

    img.save(new_pf)
    if size:
        statinfo = os.stat(new_pf)
        if statinfo.st_size > size:
            return {'error': 'too much size'}


def check_image_extension(name):
    if splitext(name)[-1] not in ('.gif', '.jpg', '.jpeg', '.png'):
        raise ValidationError("Not valid format")

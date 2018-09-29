# from os.path import splitext
# from random import choice
# from string import digits, ascii_letters

from django.db import models


class Picture(models.Model):
    image = models.ImageField(upload_to='', blank=True)


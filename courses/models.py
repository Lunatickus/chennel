from django.db import models
from django.conf import settings
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse

from utils.models import AbstractImageModel


